from daiquiri.core.exceptions import DaiquiriException


class ADQLSyntaxError(DaiquiriException):
    pass


class MySQLSyntaxError(DaiquiriException):
    pass


class PermissionError(DaiquiriException):
    pass


class TableError(DaiquiriException):
    pass

class ConnectionError(DaiquiriException):
    pass
