from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from yakumans.views import YakumanDetailView, YakumanListView

urlpatterns = [
    path("", YakumanListView.as_view(), name="yakuman-list"),
    path("<int:pk>/", YakumanDetailView.as_view(), name="yakuman-detail"),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
