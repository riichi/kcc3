from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import NotAuthenticated

from ..hmac_auth import AUTH_NAME, check_hmac_digest


class HMACAuth(BaseAuthentication):
    def __init__(self, badge_client):
        super(HMACAuth, self).__init__()
        self.badge_client = badge_client

    def authenticate(self, request):
        badge_id = request.data.get('id')
        authorization = request.META.get('HTTP_AUTHORIZATION')

        if badge_id is None:
            raise NotAuthenticated('Badge ID was not sent')
        if authorization is None:
            raise NotAuthenticated('No HMAC header')
        if not authorization.startswith(f'{AUTH_NAME} '):
            raise NotAuthenticated('Invalid Authorization method')

        digest = authorization.split()[1].strip()
        if not check_hmac_digest(
                self.badge_client.get_token(badge_id),
                request.raw_body,
                digest):
            raise NotAuthenticated('Invalid HMAC')
