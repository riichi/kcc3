from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from badges.token_generator import generate_token, MAX_TOKEN_LENGTH
from common.models import Player


class Badge(models.Model):
    id = models.SlugField(primary_key=True)

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image = models.ImageField()
    owners = models.ManyToManyField(to=User, blank=True)

    endpoint_url = models.URLField(null=True, blank=True)
    refresh_interval = models.DurationField(null=True, blank=True)
    token = models.CharField(
        null=True, max_length=MAX_TOKEN_LENGTH, default=generate_token,
        editable=False)
    periodic_task = models.OneToOneField(
        to=PeriodicTask, on_delete=models.CASCADE, null=True, editable=False)

    players = models.ManyToManyField(to=Player, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_refresh_interval = self.refresh_interval

    def get_absolute_url(self):
        return reverse('badge-detail', kwargs={'slug': self.id})

    @property
    def is_automatic(self):
        return self.endpoint_url is not None and self.token is not None

    def save(self, *args, **kwargs):
        if self.refresh_interval != self.__original_refresh_interval:
            self.__update_task()

        super(Badge, self).save(*args, **kwargs)

    def __update_task(self):
        if self.refresh_interval is None and self.periodic_task is not None:
            self.periodic_task.delete()
        elif self.refresh_interval is not None:
            self.__create_or_update_task_object()

    def __create_or_update_task_object(self):
        if self.periodic_task is None:
            task = PeriodicTask(task='kcc3.celery.debug_task')
            self.periodic_task = task
        else:
            task = self.periodic_task

        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=round(self.refresh_interval.total_seconds()),
            period=IntervalSchedule.SECONDS)
        task.interval = schedule
        task.name = f'Update {self.id} badge'

        task.save()

    def __str__(self):
        return self.title
