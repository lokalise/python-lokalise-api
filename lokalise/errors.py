"""
lokalise.errors
~~~~~~~~~~~~~~~
Defines custom exception classes.
"""

import json
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Type, Dict, cast, Union


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
        headers: Optional[Mapping[str, str]] = None,
        raw_text: Optional[str] = None,
        parsed: Optional["APIError"] = None,
    ) -> None:
        super().__init__(message, status_code)
        self.status_code = status_code
        self.message = message
        self.headers: Dict[str, str] = dict(headers or {})
        self.raw_text = raw_text
        self.parsed = parsed

    def __str__(self) -> str:
        base = f"{self.status_code} {self.message}"
        if self.parsed:
            if self.parsed.reason:
                base += f" | reason={self.parsed.reason}"
            if self.parsed.code is not None:
                base += f" | code={self.parsed.code!r}"
        return base

    @property
    def retry_after_seconds(self) -> Optional[int]:
        v = self.headers.get("Retry-After")
        if not v:
            return None
        try:
            return int(v.strip())
        except Exception:
            return None


# Тонкие классы под коды
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


ERROR_CODES: Dict[int, Type[ClientHTTPError]] = {
    400: BadRequest,
    401: Unauthorized,
    403: Forbidden,
    404: NotFound,
    405: MethodNotAllowed,
    406: NotAcceptable,
    409: Conflict,
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
    code: int | str | None
    details: dict[str, Any] | None


def _coalesce(*ss: Optional[str]) -> str:
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
    except Exception:
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
        return int(v), True
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


def parse_api_error(slurp: bytes | str, status: int) -> APIError:
    trimmed = (
        slurp.decode("utf-8", "replace") if isinstance(slurp, (bytes, bytearray)) else slurp
    ).strip()

    # Non-JSON fallback (empty or not starting with {/[)
    if not _is_probably_json(trimmed):
        message = _http_status_text(status)
        return APIError(
            status=status,
            message=message,
            reason="non-json error body" if trimmed else "empty body",
            raw=trimmed,
            code=None,
            details=None,
        )

    data = _json_loads_obj_or_none(trimmed)
    if data is None:
        return APIError(
            status=status,
            message=_http_status_text(status),
            reason="invalid json in error body",
            raw=trimmed,
            code=None,
            details={"unmarshal_error": "json decode failed"},
        )

    # 1) Top-level: {message, statusCode, error:string}
    msg1, ok_msg1 = _get_str(data, "message")
    sc1, ok_sc1 = _get_number_as_int(data, "statusCode")
    err1, ok_err1 = _get_str(data, "error")
    if ok_msg1 and ok_sc1 and ok_err1:
        return APIError(
            status=status,
            code=sc1,
            message=msg1,
            reason=err1,
            raw=trimmed,
            details=data,
        )

    # 2) Nested: {error: {message, code, details}}
    err_any = data.get("error")
    if isinstance(err_any, dict):
        msg2, _ = _get_str(err_any, "message")
        code2, ok_code2 = _get_number_as_int(err_any, "code")
        if not ok_code2:
            code2 = status
        details2 = _pick_details(err_any)
        return APIError(
            status=status,
            code=code2,
            message=_coalesce(msg2, _http_status_text(status)),
            reason="nested error",
            raw=trimmed,
            details=details2,
        )

    # 3) Alt top-level: {message, code|string|number OR errorCode, details:any}
    if ok_msg1:
        code3, ok_code3 = _get_number_as_int(data, "code")
        if ok_code3:
            return APIError(
                status=status,
                code=code3,
                message=msg1,
                reason="top-level",
                raw=trimmed,
                details=_pick_details(data),
            )
        code4, ok_code4 = _get_number_as_int(data, "errorCode")
        if ok_code4:
            return APIError(
                status=status,
                code=code4,
                message=msg1,
                reason="top-level",
                raw=trimmed,
                details=_pick_details(data),
            )

    # 4) Fallback
    reason4, _ = _get_str(data, "error")
    return APIError(
        status=status,
        code=None,
        message=_coalesce(_get_str_or(data, "message", ""), _http_status_text(status)),
        reason=_coalesce(reason4, "unhandled error format"),
        raw=trimmed,
        details=data,
    )


def error_from_http(
    status_code: int,
    *,
    message: Optional[str] = None,  # можно пробросить своё (например "GET /url failed")
    headers: Optional[Mapping[str, str]] = None,
    body_text: Optional[str] = None,
) -> ClientHTTPError:
    parsed = parse_api_error(body_text or "", status_code)
    final_message = message or parsed.message or f"HTTP {status_code} error"
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
    423: "Locked",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}


def _http_status_text(status: int) -> str:
    return _HTTP_TEXTS.get(status, f"HTTP {status} Error")
