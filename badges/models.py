from django.db import models
from django.contrib.auth.models import User

from common.models import Player


class Badge(models.Model):
    id = models.SlugField(primary_key=True)

    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()
    owners = models.ManyToManyField(to=User, blank=True)

    players = models.ManyToManyField(to=Player, blank=True)
