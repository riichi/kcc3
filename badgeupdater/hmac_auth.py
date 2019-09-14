import hmac

AUTH_NAME = 'HMAC-SHA256'


def calc_hmac_digest(token: str, body: bytes) -> str:
    return hmac.new(token.encode('utf-8'), body, 'sha256').hexdigest()


def check_hmac_digest(token: str, body: bytes, digest: str) -> bool:
    calculated_digest = calc_hmac_digest(token, body)
    return hmac.compare_digest(digest, calculated_digest)
