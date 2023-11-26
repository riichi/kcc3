from badges.local_badge_client import LocalBadgeClient, PlayerIterable
from badgeupdater.models import BadgeUpdateRequest
from chombos.models import Chombo
from players.models import Player


class ChombosBadgeClient(LocalBadgeClient):
    def get_badge_players(self, request: BadgeUpdateRequest) -> PlayerIterable:
        return Chombo.objects.values_list("player")


class ChombosInRangeClient(LocalBadgeClient):
    def get_badge_players(self, request: BadgeUpdateRequest) -> PlayerIterable:
        a = int(self.request.query_params.get("a"))
        b = self.request.query_params.get("b")
        if b is None:

            def pred(c):
                return a <= c
        else:
            b = int(b)

            def pred(c):
                return a <= c <= b

        return filter(lambda p: pred(p.chombo_set.count()), Player.objects.all())
