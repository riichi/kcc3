from django.contrib.auth.models import User
from django.db import models


class Badge(models.Model):
    id = models.SlugField(primary_key=True)

    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()


class Player(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)

    badges = models.ManyToManyField(to=Badge)
