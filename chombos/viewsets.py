from rest_framework import viewsets

from chombos.models import Chombo
from chombos.serializers import ChomboSerializer


class ChomboViewSet(viewsets.ModelViewSet):
    queryset = Chombo.objects.all()
    serializer_class = ChomboSerializer
