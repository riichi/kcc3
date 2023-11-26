import hmac

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import NotAuthenticated


class HMACAuth(BaseAuthentication):
    def __init__(self, badge_client):
        super().__init__()
        self.badge_client = badge_client

    def authenticate(self, request):
        badge_id = request.data.get("id")
        authorization = request.META.get("HTTP_AUTHORIZATION")

        if badge_id is None:
            raise NotAuthenticated("Badge ID was not sent")
        if authorization is None:
            raise NotAuthenticated("No Authorization header")
        if not authorization.startswith("Token "):
            raise NotAuthenticated("Invalid Authorization method")

        client_token = self.badge_client.get_token(badge_id)
        request_token = authorization.split()[1].strip()
        if not hmac.compare_digest(client_token, request_token):
            raise NotAuthenticated("Invalid token")
