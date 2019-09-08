from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from badges.token_generator import generate_token, MAX_TOKEN_LENGTH
from common.models import Player


class Badge(models.Model):
    id = models.SlugField(primary_key=True)

    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()
    owners = models.ManyToManyField(to=User, blank=True)

    endpoint_url = models.URLField(null=True)
    refresh_interval = models.DurationField(null=True)
    token = models.CharField(
        null=True, max_length=MAX_TOKEN_LENGTH, default=generate_token,
        editable=False)

    players = models.ManyToManyField(to=Player, blank=True)
