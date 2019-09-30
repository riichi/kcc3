from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django_hosts import reverse


class Player(models.Model):
    id = models.SlugField(primary_key=True, verbose_name='ID')

    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    nickname = models.CharField(max_length=50, blank=True)

    usma_id = models.CharField(
        max_length=30, blank=True, verbose_name='USMA ID')
    discord_id = models.CharField(
        max_length=30, blank=True, verbose_name='Discord ID')

    def clean(self):
        has_name = self.first_name and self.last_name
        has_nickname = self.nickname

        if not (has_name or has_nickname):
            raise ValidationError(
                {'first_name': 'Either full name, or nickname is required'})

    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'pk': self.pk}, host='root')

    def __str__(self):
        s = ''

        if self.first_name and self.last_name:
            s = f'{self.first_name} {self.last_name}'

        if self.nickname:
            if s:
                s += f' ({self.nickname})'
            else:
                s = self.nickname

        return s
