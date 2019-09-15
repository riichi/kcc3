from django.urls import path

from .views import PlayerDetailView

urlpatterns = [
    path('players/<int:pk>', PlayerDetailView.as_view(), name='player-detail'),
]
