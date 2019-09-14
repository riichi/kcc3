from requests import PreparedRequest
from requests.auth import AuthBase

from badgeupdater.hmac_auth import AUTH_NAME, calc_hmac_digest


class HmacAuth(AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r: PreparedRequest):
        digest = calc_hmac_digest(self.token, r.body)

        r.headers['Authorization'] = f'{AUTH_NAME} {digest}'
        return r
