"""Budget exceptions module."""


class BudgetNotFoundException(Exception):
    """BudgetNotFoundException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class BudgetNotActiveException(Exception):
    """BudgetNotActiveException class"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class StartAfterEndDateException(Exception):
    """StartAfterEndDateException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ActiveBudgetForCategoryExistsException(Exception):
    """ActiveBudgetForCategoryExistsException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TransactionBudgetTimeException(Exception):
    """TransactionBudgetTimeException class"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
