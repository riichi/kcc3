from badges.local_badge_client import (
    LocalBadgeClient, PlayerIterable)
from badgeupdater.models import BadgeUpdateRequest
from common.models import Player


class TestBadgeClient(LocalBadgeClient):
    def get_badge_players(self, request: BadgeUpdateRequest) -> PlayerIterable:
        return Player.objects.all()
