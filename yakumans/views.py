from django.views.generic import DetailView

from yakumans.models import Yakuman


class YakumanDetailView(DetailView):
    model = Yakuman
    slug_field = 'id'
