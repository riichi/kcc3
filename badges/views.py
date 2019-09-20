from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin

from badgeupdater.server.badge_updater import BadgeUpdater
from badgeupdater.server.errors import BadgeUpdateError
from players.models import Player
from .models import Badge


class BadgeRankingView(ListView):
    model = Player
    template_name = 'badges/ranking.html'

    def get_queryset(self):
        players = Player.objects.all().annotate(
            num_badges=Count('badge')).order_by('-num_badges')

        for i in range(len(players)):
            players[i].rank = i + 1

            if i > 0 and players[i].num_badges == players[i - 1].num_badges:
                players[i].rank = players[i - 1].rank

        return players


class BadgeDetailView(DetailView):
    model = Badge
    slug_field = 'id'


class UpdateBadgeBearersView(SingleObjectMixin, View):
    model = Badge
    slug_field = 'id'

    def get(self, request, *args, **kwargs):
        badge = self.get_object()

        try:
            BadgeUpdater(badge).update_badge()
            messages.info(request, 'Successfully updated the badge bearers!')
        except (IOError, BadgeUpdateError, IntegrityError) as e:
            messages.error(request, f'{e.__class__.__name__}: {e}')

        return HttpResponseRedirect(
            reverse('admin:badges_badge_change', args=[badge.pk]))
