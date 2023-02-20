class TransactionNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TransactionCashOnlyException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class IllegalParameterException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
