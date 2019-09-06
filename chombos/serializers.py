from rest_framework import serializers

from chombos.models import Chombo


class ChomboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chombo
        fields = '__all__'
