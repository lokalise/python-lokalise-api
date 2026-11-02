
"""
lokalise.request
~~~~~~~~~~~~~~~~
HTTP transport for Lokalise API requests.
"""

from typing import Any, Literal, TypedDict

import requests

from ._version import __version__
from .request_utils import format_params, path_to_endpoint
from .types import FullClientProto

Number = int | float
HttpMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
Timeout = tuple[Number | None, Number | None] | None

BASE_URL = "https://api.lokalise.com/api2/"


class RequestOptions(TypedDict):
    headers: dict[str, str]
    timeout: Timeout


def send(
    method: HttpMethod,
    url: str,
    *,
    params: dict[str, Any] | None = None,
    headers: dict[str, str],
    timeout: Timeout = None,
) -> requests.Response:
    """Send an HTTP request and return the raw response."""
    kwargs: dict[str, Any] = {
        "headers": headers,
        "timeout": timeout,
    }

    if method == "GET":
        kwargs["params"] = params
    else:
        kwargs["data"] = format_params(params)

    return requests.request(method, url, **kwargs)


def get(
    client: FullClientProto,
    path: str,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send a GET request."""
    return _send_api_request("GET", client, path, params)


def post(
    client: FullClientProto,
    path: str,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send a POST request."""
    return _send_api_request("POST", client, path, params)


def put(
    client: FullClientProto,
    path: str,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send a PUT request."""
    return _send_api_request("PUT", client, path, params)


def patch(
    client: FullClientProto,
    path: str,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send a PATCH request."""
    return _send_api_request("PATCH", client, path, params)


def delete(
    client: FullClientProto,
    path: str,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send a DELETE request."""
    return _send_api_request("DELETE", client, path, params)


def _send_api_request(
    method: HttpMethod,
    client: FullClientProto,
    path: str,
    params: dict[str, Any] | None,
) -> requests.Response:
    """Send an authenticated Lokalise API request."""
    return send(
        method,
        path_to_endpoint(client, BASE_URL, path),
        params=params,
        **options(
            client,
            method=method,
            has_body=params is not None,
        ),
    )


def base_headers(*, json_body: bool = False) -> dict[str, str]:
    """Build headers shared by all Lokalise HTTP requests."""
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
    }

    if json_body:
        headers["Content-Type"] = "application/json"

    return headers


def options(
    client: FullClientProto,
    *,
    method: HttpMethod = "GET",
    has_body: bool = False,
) -> RequestOptions:
    """Build authentication headers and timeout options."""
    headers = base_headers(
        json_body=method != "GET" and has_body
    )

    token = client.token

    if token is None:
        raise RuntimeError("Cannot build headers: API token is not set.")

    headers[client.token_header] = token

    if client.enable_compression:
        headers["Accept-Encoding"] = "gzip,deflate"

    return {
        "headers": headers,
        "timeout": _build_timeout(client),
    }


def _build_timeout(client: FullClientProto) -> Timeout:
    """Build connection and read timeout settings."""
    ct = client.connect_timeout
    rt = client.read_timeout

    if ct is None and rt is None:
        return None

    return (ct, rt)
