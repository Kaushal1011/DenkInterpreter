###############################################################################
#                                                                             #
#                                                                             #
#      BASE MODULE                                                            #
#                                                                             #
#                                                                             #
###############################################################################

from enum import Enum
_SHOULD_LOG_SCOPE = False  # see '--scope' command line option
_SHOULD_LOG_STACK = False  # see '--stack' command line option


class ErrorCode(Enum):
    UNEXPECTED_TOKEN = 'Unexpected token'
    ID_NOT_FOUND = 'Identifier not found'
    DUPLICATE_ID = 'Duplicate id found'
    VARIABLE_NOT_INITIALISER = "Variable not initialised"
    MISSING_RETURN = "Missing return statement"


class Error(Exception):
    def __init__(self, error_code=None, token=None, message=None):
        self.error_code = error_code
        self.token = token
        # add exception class name before the message
        self.message = f'{self.__class__.__name__}: {message}'


class LexerError(Error):
    pass


class ParserError(Error):
    pass


class SemanticError(Error):
    pass
