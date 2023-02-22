"""Money account exceptions module."""


class MoneyAccountNotFoundException(Exception):
    """MoneyAccountNotFoundException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MoneyAccountNotActiveException(Exception):
    """MoneyAccountNotActiveException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CurrencyNotAllowedException(Exception):
    """CurrencyNotAllowedException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class NotEnoughFundsInMoneyAccountException(Exception):
    """NotEnoughFundsInMoneyAccountException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
