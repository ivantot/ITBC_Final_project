class VendorNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class VendorNotActiveException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
