from django.urls import path

from .views import PlayerDetailView

urlpatterns = [
    path('player/<int:pk>', PlayerDetailView.as_view(), name='player-detail'),
]
