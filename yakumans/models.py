from typing import List

from django.db import models
from django_hosts import reverse

from players.models import Player
from yakumans import yakumans
from yakumans.forms import YakumansChoiceField
from yakumans.yakumans import yakuman_by_id


class YakumansField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 200
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def get_internal_type(self):
        return 'CharField'

    @staticmethod
    def __parse_yakuman_list(s: str) -> List[yakumans.Yakuman]:
        return [yakuman_by_id(yaku_id) for yaku_id in s.split(';') if yaku_id]

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value

        return self.__parse_yakuman_list(value)

    def to_python(self, value) -> List[yakumans.Yakuman]:
        if isinstance(value, list):
            return value

        if value is None:
            return []

        return self.__parse_yakuman_list(value)

    def get_prep_value(self, value):
        return ''.join(
            f'{yaku.id};' if isinstance(yaku, yakumans.Yakuman) else f'{yaku};'
            for yaku in value
        )

    def formfield(self, **kwargs):
        return YakumansChoiceField(**kwargs)


class Yakuman(models.Model):
    timestamp = models.DateTimeField(db_index=True)
    yaku = YakumansField()

    winner = models.ForeignKey(
        to=Player, on_delete=models.CASCADE,
        related_name='yakumans_won',
        help_text='The player who has got the yakuman'
    )
    loser = models.ForeignKey(
        to=Player, on_delete=models.CASCADE, null=True, blank=True,
        related_name='yakumans_lost',
        help_text='The player that has dealt in, if any'
    )
    is_tsumo = models.BooleanField()

    picture = models.ImageField(upload_to='yakumans/', blank=True)
    comment = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse(
            'yakuman-detail', host='yakumans', kwargs={'pk': self.pk}
        )

    def __str__(self):
        yaku_str = ', '.join(x.name for x in self.yaku)
        return f'{yaku_str} by {self.winner} at {self.timestamp}'
