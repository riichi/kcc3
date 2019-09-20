from django.db import models

from players.models import Player


class Chombo(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.player} at {self.timestamp}'
