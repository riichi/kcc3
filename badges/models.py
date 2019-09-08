from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

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

    players = models.ManyToManyField(to=Player, blank=True)

    def get_absolute_url(self):
        return reverse('badge-detail', kwargs={'slug': self.id})

    def __str__(self):
        return self.title
