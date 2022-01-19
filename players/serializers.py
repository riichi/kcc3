from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'id', 'first_name', 'last_name', 'nickname', 'badge_set',
            'usma_id', 'discord_id'
        ]
        read_only_fields = [
            'badge_set'
        ]
