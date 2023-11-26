from django.urls import path

from chombos.badgeclients import ChombosBadgeClient, ChombosInRangeClient

badgeclients_urlpatterns = [
    path("chombos/", ChombosBadgeClient.as_view()),
    path("in-range/", ChombosInRangeClient.as_view()),
]
