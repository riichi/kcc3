from django.urls import path

from chombos.badgeclients import ChombosBadgeClient

badgeclients_urlpatterns = [
    path('chombos/', ChombosBadgeClient.as_view()),
]
