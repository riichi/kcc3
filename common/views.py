from django.views.generic.detail import DetailView

from .models import Player


class PlayerDetailView(DetailView):
    model = Player
