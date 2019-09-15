from badges.local_badge_client import LocalBadgeClient, PlayerIterable
from badgeupdater.models import BadgeUpdateRequest
from chombos.models import Chombo


class ChombosBadgeClient(LocalBadgeClient):
    def get_badge_players(self, request: BadgeUpdateRequest) -> PlayerIterable:
        return Chombo.objects.values_list('player')
