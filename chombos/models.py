from django.db import models

from players.models import Player


class Chombo(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True)
    comment = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=3, decimal_places=1, default=1)

    def __str__(self):
        return f"{self.player} at {self.timestamp}"
