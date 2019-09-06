from rest_framework import viewsets
from .models import Badge
from .serializers import BadgeSerializer


class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer