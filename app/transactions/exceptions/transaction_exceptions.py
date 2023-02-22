"""Transactions exceptions module."""


class TransactionNotFoundException(Exception):
    """TransactionNotFoundException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TransactionCashOnlyException(Exception):
    """TransactionCashOnlyException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class IllegalParameterException(Exception):
    """IllegalParameterException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
