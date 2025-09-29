"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.

Attributes:

    :attribute str BASE_URL: path to the Lokalise APIv2.
    :attribute list PAGINATION_HEADERS: list of response headers that contain pagination data.
"""

from typing import Any

import requests

from ._version import __version__
from .request_utils import format_params, path_to_endpoint, raise_on_error
from .types import FullClientProto

BASE_URL = "https://api.lokalise.com/api2/"
PAGINATION_HEADERS = [
    "x-pagination-total-count",
    "x-pagination-page-count",
    "x-pagination-limit",
    "x-pagination-page",
    "x-pagination-next-cursor",
]


def get(client: FullClientProto, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """Performs GET requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(
        requests.get(path_to_endpoint(client, BASE_URL, path), params=params, **options(client))
    )


def post(
    client: FullClientProto, path: str, params: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Performs POST requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(
        requests.post(
            path_to_endpoint(client, BASE_URL, path),
            data=format_params(params),
            **options(client, method="POST", has_body=params is not None),
        )
    )


def put(client: FullClientProto, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """Performs PUT requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(
        requests.put(
            path_to_endpoint(client, BASE_URL, path),
            data=format_params(params),
            **options(client, method="PUT", has_body=params is not None),
        )
    )


def patch(
    client: FullClientProto, path: str, params: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Performs PATCH requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(
        requests.patch(
            path_to_endpoint(client, BASE_URL, path),
            data=format_params(params),
            **options(client, method="PATCH", has_body=params is not None),
        )
    )


def delete(
    client: FullClientProto, path: str, params: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Performs DELETE requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(
        requests.delete(
            path_to_endpoint(client, BASE_URL, path),
            data=format_params(params),
            **options(client, method="DELETE", has_body=params is not None),
        )
    )


def respond_with(response: requests.Response) -> dict[str, Any]:
    """Converts the response data to JSON and attaches pagination-related data.
    An exception will be raised if the response status code is 4xx or 5xx,
    or contains an "error" key

    :param response: Response from the API
    :rtype dict:
    """
    try:
        data: dict[str, Any] = response.json()
    except ValueError:
        data = {"_raw_body": response.text}

    raise_on_error(response, data)

    return {**data, **extract_headers_from(response)}


def extract_headers_from(response: requests.Response) -> dict[str, Any]:
    """
    Pull pagination metadata (and the oversized flag) out of an HTTP response.

    Returns a dict like:
    {
        "_pagination": { "x-pagination-page": "3", ... },
        "_response_too_big": True   # only when x-response-too-big header is present
    }
    """

    headers_lower = {k.lower(): v for k, v in response.headers.items()}

    pagination = {k: v for k, v in headers_lower.items() if k in PAGINATION_HEADERS}

    result: dict[str, Any] = {"_pagination": pagination}

    if "x-response-too-big" in headers_lower:
        result["_response_too_big"] = True

    return result


def options(
    client: FullClientProto, *, method: str = "GET", has_body: bool = False
) -> dict[str, Any]:
    """Prepares proper request options, including Accept headers, API token,
    and timeouts. Raises RuntimeError if client.token is None.

    :param client: Lokalise API client
    :type client: lokalise.Client
    :rtype dict:
    """
    headers: dict[str, str] = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
    }
    
    if client.token is None:
        raise RuntimeError("Cannot build headers: API token is not set. Did you call reset_client()?")

    headers[client.token_header] = client.token

    if client.enable_compression:
        headers["Accept-Encoding"] = "gzip,deflate,br"

    if method != "GET" and has_body:
        headers["Content-Type"] = "application/json"

    return {
        "timeout": _build_timeout(client),
        "headers": headers,
    }


def _build_timeout(client: FullClientProto) -> float | tuple[float, float] | None:
    """Return proper timeout value for requests.

    - None - wait indefinitely
    - float - apply to both connect and read
    - (connect, read) tuple - set individually
    """
    ct = client.connect_timeout
    rt = client.read_timeout

    if ct is None and rt is None:
        return None
    if ct is not None and rt is not None:
        return (ct, rt)

    return ct if ct is not None else rt