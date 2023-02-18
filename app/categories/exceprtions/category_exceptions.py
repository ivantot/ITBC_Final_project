class CategoryNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CategoryNotActiveException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
