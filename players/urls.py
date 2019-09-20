from django.urls import path

from .views import PlayerDetailView

urlpatterns = [
    path('<slug:pk>/', PlayerDetailView.as_view(), name='player-detail'),
]
