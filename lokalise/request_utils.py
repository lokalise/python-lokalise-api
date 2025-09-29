"""
lokalise.request_utils
~~~~~~~~~~~~~~~~~~~~~~
This module provides helpers to send HTTP requests.
"""

import json
from collections.abc import Mapping
from typing import Any, NoReturn

from requests import Response

from . import errors
from .types import HasApiHost


def raise_on_error(response: Response, data: Mapping[str, Any] | None) -> None:
    """Raises an error for HTTP codes 400+"""
    has_error_flag = isinstance(data, Mapping) and "error" in data
    is_error_status = response.status_code >= 400
    if not (is_error_status or has_error_flag):
        return

    status = response.status_code if is_error_status else 400

    hint = None
    try:
        method = getattr(response.request, "method", None)
        url = getattr(response.request, "url", None)
        if method and url:
            hint = f"{method} {url} failed"
    except Exception:  # pragma: no cover
        pass  # pragma: no cover

    respond_with_error(
        data if isinstance(data, Mapping) else None,
        status,
        headers=response.headers,
        message_hint=hint,
    )


def respond_with_error(
    data: Mapping[str, Any] | None,
    status_code: int,
    *,
    headers: Mapping[str, str] | None = None,
    message_hint: str | None = None,
) -> NoReturn:
    """Raises an error based on the HTTP status code.
    If the status code is unknown, raises a generic ClientError

    :param data: Response body from the API that usually contains error message
    :param code: Response status code
    """
    if data and "_raw_body" in data:
        body_text = data["_raw_body"]
    else:
        body_text = json.dumps(data, ensure_ascii=False) if data is not None else ""
    raise errors.error_from_http(
        status_code,
        message=message_hint,
        headers=headers,
        body_text=body_text,
    )


def path_to_endpoint(client: HasApiHost, default_base_uri: str, path: str) -> str:
    """Prepares the full URI to send request to."""
    base_uri = client.api_host or default_base_uri
    return join_url(base_uri, path)


def format_params(params: dict[str, Any] | None = None) -> str | None:
    """Converts request params to a JSON string for the request body."""
    return json.dumps(params) if params is not None else None


def join_url(base: str, path: str) -> str:
    """
    Safe join for base URL and path
    """
    url = base.rstrip("/") + "/" + path.lstrip("/")
    return url.rstrip("/")
