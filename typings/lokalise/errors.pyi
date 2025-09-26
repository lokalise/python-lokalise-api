class ClientError(Exception): ...

class ClientHTTPError(ClientError):
    status_code: int
    headers: dict[str, str]
    raw_text: str | None
    parsed: APIError | None

class BadRequest(ClientHTTPError): ...
class Unauthorized(ClientHTTPError): ...
class Forbidden(ClientHTTPError): ...
class NotFound(ClientHTTPError): ...
class MethodNotAllowed(ClientHTTPError): ...
class NotAcceptable(ClientHTTPError): ...
class Conflict(ClientHTTPError): ...
class Locked(ClientHTTPError): ...
class TooManyRequests(ClientHTTPError): ...
class ServerError(ClientHTTPError): ...
class BadGateway(ClientHTTPError): ...
class ServiceUnavailable(ClientHTTPError): ...
class GatewayTimeout(ClientHTTPError): ...

class APIError:
    status: int
    message: str
    reason: str
    raw: str
    code: int | str | None
    details: dict[str, object] | None

__all__ = [
    "ClientError",
    "ClientHTTPError",
    "BadRequest",
    "Unauthorized",
    "Forbidden",
    "NotFound",
    "MethodNotAllowed",
    "NotAcceptable",
    "Conflict",
    "Locked",
    "TooManyRequests",
    "ServerError",
    "BadGateway",
    "ServiceUnavailable",
    "GatewayTimeout",
    "APIError",
]
