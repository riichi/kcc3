from abc import ABC
from typing import Union, List, Iterable

from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

from badges.models import Badge
from badgeupdater.client.badge_client import BadgeClient
from badgeupdater.models import BadgeUpdateRequest
from players.models import Player

PlayerIterable = Iterable[Union[int, Player]]


class BadgeDoesNotExist(APIException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = 'The Badge with given ID does not exist'


class LocalBadgeClient(BadgeClient, ABC):
    def get_token(self, badge_id: str) -> str:
        try:
            return Badge.objects.get(id=badge_id).token
        except Badge.DoesNotExist:
            raise BadgeDoesNotExist

    def get_badge_player_ids(self, request: BadgeUpdateRequest) -> List[int]:
        return list(map(
            lambda x: x.id if isinstance(x, Player) else x,
            self.get_badge_players(request)))

    def get_badge_players(self, request: BadgeUpdateRequest) -> PlayerIterable:
        raise NotImplementedError
