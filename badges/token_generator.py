from django.utils.crypto import get_random_string

MAX_TOKEN_LENGTH = 64


def generate_token():
    return get_random_string(MAX_TOKEN_LENGTH)
