"""Users exceptions module."""


class UserHasRoleNotFoundException(Exception):
    """UserHasRoleNotFoundException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
