from rest_framework import serializers

from badgeupdater.models import BadgeUpdateRequest, BadgeUpdateResponse


class BadgeUpdateRequestSerializer(serializers.Serializer):
    id = serializers.SlugField()

    def create(self, validated_data) -> BadgeUpdateRequest:
        return BadgeUpdateRequest(**validated_data)


class BadgeUpdateResponseSerializer(serializers.Serializer):
    players = serializers.ListField(child=serializers.SlugField())

    def create(self, validated_data) -> BadgeUpdateResponse:
        return BadgeUpdateResponse(**validated_data)
