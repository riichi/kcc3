from django.views.generic import DetailView, ListView

from yakumans.models import Yakuman


class YakumanListView(ListView):
    model = Yakuman
    ordering = ("-timestamp",)


class YakumanDetailView(DetailView):
    model = Yakuman
    slug_field = "id"
