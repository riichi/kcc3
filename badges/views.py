from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView, SingleObjectMixin

from badgeupdater.server.badge_updater import BadgeUpdater
from badgeupdater.server.errors import BadgeUpdateError
from .models import Badge


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
