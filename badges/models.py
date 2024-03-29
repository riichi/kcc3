import json

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from django_hosts import reverse

from badges.token_generator import MAX_TOKEN_LENGTH, generate_token
from badges.validators import (
    ImageMaxResolutionValidator,
    ImageMinResolutionValidator,
    MaxFileSizeValidator,
    image_square_validator,
)
from players.models import Player

MIN_RES = settings.BADGE_IMAGE_MIN_RES
MAX_RES = settings.BADGE_IMAGE_MAX_RES
MAX_SIZE = settings.BADGE_IMAGE_MAX_SIZE


class BadgeQuerySet(models.QuerySet):
    not_automatic_q = Q(endpoint_url__isnull=True) | Q(endpoint_url__exact="")

    def automatic(self):
        return self.exclude(self.not_automatic_q)

    def not_automatic(self):
        return self.filter(self.not_automatic_q)


class Badge(models.Model):
    id = models.SlugField(primary_key=True, verbose_name="ID")

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image = models.ImageField(
        help_text=f"The image must be square between {MIN_RES}x{MIN_RES} and "
        f"{MAX_RES}x{MAX_RES} and must not exceed "
        f"{MaxFileSizeValidator.human_readable_size(MAX_SIZE)}.",
        validators=[
            ImageMinResolutionValidator(MIN_RES),
            ImageMaxResolutionValidator(MAX_RES),
            image_square_validator,
            MaxFileSizeValidator(MAX_SIZE),
        ],
    )
    owners = models.ManyToManyField(to=User, blank=True)

    endpoint_url = models.URLField(blank=True, verbose_name="Endpoint URL")
    refresh_interval = models.DurationField(null=True, blank=True)
    token = models.CharField(blank=True, max_length=MAX_TOKEN_LENGTH, default=generate_token, editable=False)
    periodic_task = models.OneToOneField(to=PeriodicTask, on_delete=models.CASCADE, null=True, editable=False)

    players = models.ManyToManyField(to=Player, blank=True)

    objects = BadgeQuerySet.as_manager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_refresh_interval = self.refresh_interval

    def get_absolute_url(self):
        return reverse("badge-detail", kwargs={"slug": self.id}, host="root")

    @property
    def is_automatic(self):
        return bool(self.endpoint_url and self.token)

    def save(self, *args, **kwargs):
        if self.refresh_interval != self.__original_refresh_interval:
            self.__update_task()

        super().save(*args, **kwargs)

    def __update_task(self):
        if self.refresh_interval is None and self.periodic_task is not None:
            self.periodic_task.delete()
        elif self.refresh_interval is not None:
            self.__create_or_update_task_object()

    def __create_or_update_task_object(self):
        if self.periodic_task is None:
            kwargs = {"badge_id": self.id}
            task = PeriodicTask(task="badgeupdater.server.tasks.update_badge_task", kwargs=json.dumps(kwargs))
        else:
            task = self.periodic_task

        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=round(self.refresh_interval.total_seconds()), period=IntervalSchedule.SECONDS
        )
        task.interval = schedule
        task.name = f"Update {self.id} badge"

        task.save()
        self.periodic_task = task

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Badge)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.periodic_task:
        instance.periodic_task.delete()
