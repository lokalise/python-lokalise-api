"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.

Attributes:

    :attribute str BASE_URL: path to the Lokalise APIv2.
    :attribute list PAGINATION_HEADERS: list of response headers that contain pagination data.
"""

from typing import Any, Optional

from .types import FullClientProto

import requests

from .request_utils import format_params, path_to_endpoint, raise_on_error

from ._version import __version__

BASE_URL = "https://api.lokalise.com/api2/"
PAGINATION_HEADERS = [
    "x-pagination-total-count",
    "x-pagination-page-count",
    "x-pagination-limit",
    "x-pagination-page",
    "x-pagination-next-cursor",
]


def get(
    client: FullClientProto, path: str, params: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
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
    client: FullClientProto, path: str, params: Optional[dict[str, Any]] = None
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
            **options(client),
        )
    )


def put(
    client: FullClientProto, path: str, params: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
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
            **options(client),
        )
    )


def patch(
    client: FullClientProto, path: str, params: Optional[dict[str, Any]] = None
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
            **options(client),
        )
    )


def delete(
    client: FullClientProto, path: str, params: Optional[dict[str, Any]] = None
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
            **options(client),
        )
    )


def respond_with(response: requests.models.Response) -> dict[str, Any]:
    """Converts the response data to JSON and attaches pagination-related data.
    An exception will be raised if the response status code is 4xx or 5xx,
    or contains an "error" key

    :param response: Response from the API
    :rtype dict:
    """
    data = response.json()
    raise_on_error(response, data)

    return {**data, **extract_headers_from(response)}


def extract_headers_from(response: requests.models.Response) -> dict[str, Any]:
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


def options(client: FullClientProto) -> dict[str, Any]:
    """Prepares proper request options, including Accept headers, API token,
    and timeouts.

    :param client: Lokalise API client
    :type client: lokalise.Client
    :rtype dict:
    """
    headers: dict[str, Any] = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
        "Accept-Encoding": None,
    }
    headers[client.token_header] = client.token
    if client.enable_compression:
        headers["Accept-Encoding"] = "gzip,deflate,br"

    timeout_tuple: tuple[float | int | None, float | int | None] = (
        client.connect_timeout,
        client.read_timeout,
    )

    return {"timeout": timeout_tuple, "headers": headers}
