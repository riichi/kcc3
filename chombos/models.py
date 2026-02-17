from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from players.models import Player


class Chombo(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True)
    comment = models.TextField(blank=True)
    weight = models.DecimalField(
        max_digits=2, decimal_places=1, default=1, validators=[MinValueValidator(1), MaxValueValidator(6)]
    )

    def __str__(self):
        return f"{self.player} at {self.timestamp}"
