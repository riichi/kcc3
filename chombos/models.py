from django.db import models

from common.models import Player


class Chombo(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True)
    comment = models.TextField()
