from django.urls import path

from .views import BadgeDetailView

urlpatterns = [
    path('<slug:slug>/', BadgeDetailView.as_view(), name='badge-detail'),
]
