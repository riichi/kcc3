from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from yakumans.views import YakumanDetailView

urlpatterns = [
    path('<int:pk>/', YakumanDetailView.as_view(), name='yakuman-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
