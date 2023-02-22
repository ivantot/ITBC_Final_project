"""Users exceptions module."""


class UserNotFoundException(Exception):
    """UserNotFoundException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    """UserInvalidPassword class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotActiveException(Exception):
    """UserNotActiveException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
