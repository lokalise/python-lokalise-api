"""
lokalise.errors
~~~~~~~~~~~~~~~
Defines custom exception classes.
"""

import json
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Union, cast

JSONValue = Union[str, int, float, bool, None, "JSONObject", "JSONList"]
JSONList = list[JSONValue]
JSONObject = dict[str, JSONValue]


class ClientError(Exception):
    """Base SDK error."""


class ClientHTTPError(ClientError):
    """
    HTTP error with structured payload info (if we could parse it).
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        *,
        headers: Mapping[str, str] | None = None,
        raw_text: str | None = None,
        parsed: "APIError | None" = None,
    ) -> None:
        super().__init__(message, status_code)
        self.status_code = status_code
        self.message = message
        self.headers: dict[str, str] = dict(headers or {})
        self.raw_text: str | None = raw_text
        self.parsed: APIError | None = parsed

    def __str__(self) -> str:
        base = f"{self.status_code} {self.message}"
        if self.parsed:
            if self.parsed.reason:
                base += f" | reason={self.parsed.reason}"
            if self.parsed.code is not None:
                base += f" | code={self.parsed.code!r}"
        return base


class BadRequest(ClientHTTPError): ...


class Unauthorized(ClientHTTPError): ...


class Forbidden(ClientHTTPError): ...


class NotFound(ClientHTTPError): ...


class MethodNotAllowed(ClientHTTPError): ...


class NotAcceptable(ClientHTTPError): ...


class Conflict(ClientHTTPError): ...


class ContentTooLarge(ClientHTTPError): ...


class Locked(ClientHTTPError): ...


class TooManyRequests(ClientHTTPError): ...


class ServerError(ClientHTTPError): ...


class BadGateway(ClientHTTPError): ...


class ServiceUnavailable(ClientHTTPError): ...


class GatewayTimeout(ClientHTTPError): ...


ERROR_CODES: dict[int, type[ClientHTTPError]] = {
    400: BadRequest,
    401: Unauthorized,
    403: Forbidden,
    404: NotFound,
    405: MethodNotAllowed,
    406: NotAcceptable,
    409: Conflict,
    413: ContentTooLarge,
    423: Locked,
    429: TooManyRequests,
    500: ServerError,
    502: BadGateway,
    503: ServiceUnavailable,
    504: GatewayTimeout,
}


@dataclass
class APIError:
    status: int
    message: str
    reason: str
    raw: str
    code: int | None
    details: dict[str, Any] | None


def _coalesce(*ss: str | None) -> str:
    for s in ss:
        if s:
            return s
    return ""


def _is_probably_json(trimmed: str) -> bool:
    return bool(trimmed) and trimmed[0] in "{["


def _json_loads_obj_or_none(trimmed: str) -> JSONObject | None:
    try:
        obj = json.loads(trimmed)
        if isinstance(obj, dict):
            return cast(JSONObject, obj)
    except json.JSONDecodeError:
        return None


def _get_str(m: Mapping[str, JSONValue], key: str) -> tuple[str, bool]:
    v = m.get(key)
    if isinstance(v, str):
        return v, True
    return "", False


def _get_str_or(m: Mapping[str, JSONValue], key: str, default: str) -> str:
    s, ok = _get_str(m, key)
    return s if ok else default


def _as_int_maybe(v: Any) -> tuple[int, bool]:
    if isinstance(v, bool):
        return 0, False
    if isinstance(v, int):
        return v, True
    if isinstance(v, float):
        if v.is_integer():
            return int(v), True
        return 0, False
    if isinstance(v, str):
        s = v.strip()
        if s.isdigit() or (s.startswith(("+", "-")) and s[1:].isdigit()):
            try:
                return int(s), True
            except Exception:
                return 0, False
        return 0, False
    return 0, False


def _get_number_as_int(m: Mapping[str, JSONValue], key: str) -> tuple[int, bool]:
    return _as_int_maybe(m.get(key))


def _pick_details(obj: Mapping[str, JSONValue]) -> JSONObject:
    det = obj.get("details")
    if isinstance(det, dict):
        return det
    if det is not None:
        return {"details": det}
    return {"reason": "server error without details"}


def parse_api_error(
    slurp: bytes | bytearray | str,
    status: int,
) -> APIError:
    trimmed = _decode_error_body(slurp)

    if not _is_probably_json(trimmed):
        return _non_json_error(trimmed, status)

    data = _json_loads_obj_or_none(trimmed)

    if data is None:
        return _invalid_json_error(trimmed, status)

    parsers = (
        _parse_standard_error,
        _parse_nested_error,
        _parse_top_level_error,
        _parse_oauth_error,
    )

    for parser in parsers:
        parsed = parser(data, status, trimmed)
        if parsed is not None:
            return parsed

    return _parse_fallback_error(data, status, trimmed)


def _decode_error_body(slurp: bytes | bytearray | str) -> str:
    if isinstance(slurp, (bytes, bytearray)):
        return slurp.decode("utf-8", "replace").strip()

    return slurp.strip()


def _non_json_error(raw: str, status: int) -> APIError:
    return APIError(
        status=status,
        message=_http_status_text(status),
        reason="non-json error body" if raw else "empty body",
        raw=raw,
        code=None,
        details=None,
    )


def _invalid_json_error(raw: str, status: int) -> APIError:
    return APIError(
        status=status,
        message=_http_status_text(status),
        reason="invalid json in error body",
        raw=raw,
        code=None,
        details={"unmarshal_error": "json decode failed"},
    )


def _parse_standard_error(
    data: JSONObject,
    status: int,
    raw: str,
) -> APIError | None:
    message, has_message = _get_str(data, "message")
    status_code, has_status_code = _get_number_as_int(data, "statusCode")
    error, has_error = _get_str(data, "error")

    if not (has_message and has_status_code and has_error):
        return None

    return APIError(
        status=status,
        code=status_code,
        message=message,
        reason=error,
        raw=raw,
        details=data,
    )


def _parse_nested_error(
    data: JSONObject,
    status: int,
    raw: str,
) -> APIError | None:
    error = data.get("error")

    if not isinstance(error, dict):
        return None

    message, _ = _get_str(error, "message")
    code, has_code = _get_number_as_int(error, "code")

    return APIError(
        status=status,
        code=code if has_code else status,
        message=_coalesce(message, _http_status_text(status)),
        reason="nested error",
        raw=raw,
        details=_pick_details(error),
    )


def _parse_top_level_error(
    data: JSONObject,
    status: int,
    raw: str,
) -> APIError | None:
    message, has_message = _get_str(data, "message")

    if not has_message:
        return None

    for key in ("code", "errorCode"):
        code, has_code = _get_number_as_int(data, key)

        if has_code:
            return APIError(
                status=status,
                code=code,
                message=message,
                reason="top-level",
                raw=raw,
                details=_pick_details(data),
            )

    return None


def _parse_oauth_error(
    data: JSONObject,
    status: int,
    raw: str,
) -> APIError | None:
    error, has_error = _get_str(data, "error")
    description, has_description = _get_str(
        data,
        "error_description",
    )

    if not (has_error and has_description):
        return None

    return APIError(
        status=status,
        code=None,
        message=description,
        reason=error,
        raw=raw,
        details=data,
    )


def _parse_fallback_error(
    data: JSONObject,
    status: int,
    raw: str,
) -> APIError:
    reason, _ = _get_str(data, "error")

    return APIError(
        status=status,
        code=None,
        message=_coalesce(
            _get_str_or(data, "message", ""),
            _http_status_text(status),
        ),
        reason=_coalesce(reason, "unhandled error format"),
        raw=raw,
        details=data,
    )


def error_from_http(
    status_code: int,
    *,
    message: str | None = None,
    headers: Mapping[str, str] | None = None,
    body_text: str | None = None,
) -> ClientHTTPError:
    parsed = parse_api_error(body_text or "", status_code)

    final_message = parsed.message or f"HTTP {status_code} error"

    if message:
        final_message = f"{final_message} ({message})"

    cls = ERROR_CODES.get(status_code, ClientHTTPError)
    return cls(
        final_message,
        status_code,
        headers=headers,
        raw_text=body_text,
        parsed=parsed,
    )


_HTTP_TEXTS = {
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    409: "Conflict",
    413: "Content Too Large",
    423: "Locked",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}


def _http_status_text(status: int) -> str:
    return _HTTP_TEXTS.get(status, f"HTTP {status} Error")
