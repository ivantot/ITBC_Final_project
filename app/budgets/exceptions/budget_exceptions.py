class BudgetNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BudgetNotActiveException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
