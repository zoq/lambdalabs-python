class APIException(Exception):
    """This exception is raised if there was an error from Lambda Labs API.
    Could be an invalid input, token etc.

    Raised when an API HTTP call response has a status code >= 400
    """

    def __init__(self, code: str, message: str) -> None:
        """
        Initialize an APIException object

        :param code: error code
        :type code: str
        :param message: error message
        :type message: str
        """
        self.code = code
        self.message = message

    def __str__(self) -> str:
        msg = ""
        if self.code:
            msg = f'error code: {self.code}\n'
        msg += f'message: {self.message}'

        return msg
