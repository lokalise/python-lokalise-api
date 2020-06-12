class ClientError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg, code)
        self.message = msg
        self.code = code



class BadRequest(ClientError):
    pass


class Unauthorized(ClientError):
    pass


class Forbidden(ClientError):
    pass


class NotFound(ClientError):
    pass


class MethodNowAllowed(ClientError):
    pass


class NotAcceptable(ClientError):
    pass


class Conflict(ClientError):
    pass


class Locked(ClientError):
    pass


class TooManyRequests(ClientError):
    pass


class ServerError(ClientError):
    pass


class BadGateway(ClientError):
    pass


class ServiceUnavailable(ClientError):
    pass


class GatewayTimeout(ClientError):
    pass


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
