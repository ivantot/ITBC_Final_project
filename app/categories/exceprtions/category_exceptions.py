"""Categories exceptions module."""


class CategoryNotFoundException(Exception):
    """CategoryNotFoundException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CategoryNotActiveException(Exception):
    """CategoryNotActiveException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
