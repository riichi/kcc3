from django.urls import path

from badges.badgeclients import TestBadgeClient
from .views import BadgeDetailView, UpdateBadgeBearersView

urlpatterns = [
    path('<slug:slug>/', BadgeDetailView.as_view(), name='badge-detail'),
]

admin_urlpatters = [
    path(
        'badge/<slug:slug>/update_bearers/',
        UpdateBadgeBearersView.as_view(),
        name='update-badge-bearers'),
]

badgeclients_urlpatterns = [
    path('test/', TestBadgeClient.as_view()),
]
