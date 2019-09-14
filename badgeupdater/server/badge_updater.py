import requests
from rest_framework.exceptions import ValidationError

from badges.models import Badge
from badgeupdater.models import BadgeUpdateRequest, BadgeUpdateResponse
from badgeupdater.serializers import (
    BadgeUpdateRequestSerializer, BadgeUpdateResponseSerializer)
from badgeupdater.server.auth import HmacAuth
from badgeupdater.server.errors import BadgeUpdateError


class BadgeUpdater:
    def __init__(self, badge: Badge):
        assert badge.endpoint_url, 'Endpoint URL was not provided'
        assert badge.token, 'Authorization token was not generated'

        self.badge = badge

    def update_badge(self):
        body = self.__create_message_body()
        response = requests.post(
            self.badge.endpoint_url,
            json=body,
            auth=HmacAuth(self.badge.token))

        if not response.ok:
            raise BadgeUpdateError(response.content, response.status_code)

        update_response = self.__get_update_response(response)
        self.badge.players.set(update_response.players)

    @staticmethod
    def __get_update_response(response) -> BadgeUpdateResponse:
        serializer = BadgeUpdateResponseSerializer(data=response.json())

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise BadgeUpdateError(
                f'remote server sent an invalid response: {e}')

        return serializer.save()

    def __create_message_body(self):
        request = BadgeUpdateRequest(
            id=self.badge.id)
        serializer = BadgeUpdateRequestSerializer(instance=request)

        return serializer.data
