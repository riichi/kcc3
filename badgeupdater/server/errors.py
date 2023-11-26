class BadgeUpdateError(Exception):
    def __init__(self, message, status_code=None):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        message = self.message
        if self.status_code is not None:
            message = f"HTTP {self.status_code}, body: {message}"

        return f"Could not update badge: {message}"
