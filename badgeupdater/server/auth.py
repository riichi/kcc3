from requests import PreparedRequest
from requests.auth import AuthBase


class HmacAuth(AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r: PreparedRequest):
        r.headers['Authorization'] = f'Token {self.token}'

        return r
