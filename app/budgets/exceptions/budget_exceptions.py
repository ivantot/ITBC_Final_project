class BudgetNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BudgetNotActiveException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class StartAfterEndDateException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ActiveBudgetForCategoryExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TransactionBudgetTimeException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
