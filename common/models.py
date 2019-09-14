from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Player(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    usma_id = models.CharField(max_length=30, null=True)

    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
