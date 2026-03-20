from collections.abc import Mapping
from typing import Any

JSONObject = dict[str, JSONValue]
JSONList = list[JSONValue]
JSONValue = str | int | float | bool | None | JSONObject | JSONList

class ClientError(Exception): ...

class APIError:
    status: int
    message: str
    reason: str
    raw: str
    code: int | str | None
    details: dict[str, Any] | None

    def __init__(
        self,
        status: int,
        message: str,
        reason: str,
        raw: str,
        code: int | str | None,
        details: dict[str, Any] | None,
    ) -> None: ...

class ClientHTTPError(ClientError):
    status_code: int
    headers: dict[str, str]
    raw_text: str | None
    parsed: APIError | None
    message: str

    def __init__(
        self,
        message: str,
        status_code: int,
        *,
        headers: Mapping[str, str] | None = None,
        raw_text: str | None = None,
        parsed: APIError | None = None,
    ) -> None: ...

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

def error_from_http(
    status_code: int,
    *,
    message: str | None = None,
    headers: Mapping[str, str] | None = None,
    body_text: str | None = None,
) -> ClientHTTPError: ...
def parse_api_error(slurp: bytes | str, status: int) -> APIError: ...
def _coalesce(*ss: str | None) -> str: ...
def _as_int_maybe(v: Any) -> tuple[int, bool]: ...
def _pick_details(obj: Mapping[str, JSONValue]) -> JSONObject: ...

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
    "parse_api_error",
    "error_from_http",
]
