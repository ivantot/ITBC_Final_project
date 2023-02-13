class CategoryNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CategoryTypeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CategoryTypeExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
