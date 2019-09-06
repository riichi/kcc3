from django.db import models

from common.models import Player


class Badge(models.Model):
    id = models.SlugField(primary_key=True)

    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()

    players = models.ManyToManyField(to=Player)
