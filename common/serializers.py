from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name']