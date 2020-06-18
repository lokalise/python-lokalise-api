"""
lokalise.errors
~~~~~~~~~~~~~~~
Defines custom exception classes.
"""
from typing import Union


class ClientError(Exception):
    """General exception class.
    """

    def __init__(self, msg: str, code: Union[str, int]) -> None:
        """Initializes a new exception.

        :param msg: Exception message
        :param code: Exception code (derived from HTTP status code)
        """
        super().__init__(msg, code)
        self.message = msg
        self.code = code


class BadRequest(ClientError):
    """The provided request is incorrect,
    often due to missing a required parameter. HTTP status code 400.
    """


class Unauthorized(ClientError):
    """API token is incorrect. HTTP status code 401.
    """


class Forbidden(ClientError):
    """The authenticated user does not have sufficient rights to perform the
    desired action. HTTP status code 403.
    """


class NotFound(ClientError):
    """The provided endpoint (resource) cannot be found. HTTP status code 404.
    """


class MethodNowAllowed(ClientError):
    """HTTP request with the provided verb is not supported by the endpoint.
    HTTP status code 405.
    """


class NotAcceptable(ClientError):
    """Posted resource is malformed. HTTP status code 406.
    """


class Conflict(ClientError):
    """Request conflicts with another request. HTTP status code 409.
    """


class Locked(ClientError):
    """Your token is used simultaneously in multiple requests.
    HTTP status code 423.
    """


class TooManyRequests(ClientError):
    """Too many requests hit the API too quickly. HTTP status code 429.
    """


class ServerError(ClientError):
    """Server-side error. HTTP status code 500.
    """


class BadGateway(ClientError):
    """Server-side error. HTTP status code 502.
    """


class ServiceUnavailable(ClientError):
    """Server is not available at the moment. HTTP status code 503.
    """


class GatewayTimeout(ClientError):
    """Server has not responded in a timely fashion. HTTP status code 504.
    """


ERROR_CODES = {
    400: BadRequest,
    401: Unauthorized,
    403: Forbidden,
    404: NotFound,
    405: MethodNowAllowed,
    406: NotAcceptable,
    409: Conflict,
    423: Locked,
    429: TooManyRequests,
    500: ServerError,
    502: BadGateway,
    503: ServiceUnavailable,
    504: GatewayTimeout
}
