class EmployeeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotSuperUser(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
