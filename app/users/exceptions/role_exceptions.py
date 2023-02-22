"""Users exceptions module."""


class RoleNotFoundException(Exception):
    """RoleNotFoundException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
