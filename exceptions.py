class CodeRequestError(Exception):
    """Status code error"""


class ResultRequestError(Exception):
    """Result in source response is not True"""


class ResultErrorsReturned(Exception):
    """Source return errors in response"""


class ConfirmationCodeParseError(Exception):
    """Error due parse confirmation code"""
