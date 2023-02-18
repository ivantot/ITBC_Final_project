class MoneyAccountNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MoneyAccountNotActiveException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
