"""Vendors exceptions module."""


class VendorNotFoundException(Exception):
    """VendorNotFoundException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class VendorNotActiveException(Exception):
    """VendorNotActiveException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
