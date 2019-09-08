from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Badge


class BadgeDetailView(DetailView):
    model = Badge
    slug_field = 'id'
