from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
