from typing import List

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from badgeupdater.client.auth import HMACAuth
from badgeupdater.client.parsers import BodyJSONParser
from badgeupdater.models import BadgeUpdateRequest, BadgeUpdateResponse
from badgeupdater.serializers import (
    BadgeUpdateRequestSerializer, BadgeUpdateResponseSerializer)


class BadgeClient(APIView):
    parser_classes = (BodyJSONParser,)

    def post(self, request: Request, format=None):
        update_request = self.__get_update_request(request)
        response = self.__create_response(update_request)

        serializer = BadgeUpdateResponseSerializer(instance=response)
        return Response(serializer.data)

    @staticmethod
    def __get_update_request(request: Request) -> BadgeUpdateRequest:
        serializer = BadgeUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return serializer.save()

    def __create_response(self, badge_update_request: BadgeUpdateRequest):
        players = self.get_badge_player_ids(badge_update_request)

        return BadgeUpdateResponse(players)

    def get_authenticators(self):
        return HMACAuth(self),

    def get_badge_player_ids(self, request: BadgeUpdateRequest) -> List[str]:
        raise NotImplementedError

    def get_token(self, badge_id: str) -> str:
        raise NotImplementedError
