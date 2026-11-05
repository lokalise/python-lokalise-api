"""
lokalise.request_utils
~~~~~~~~~~~~~~~~~~~~~~
This module provides helpers to send HTTP requests.
"""

import json
from .types import HasApiHost, JsonBody


def path_to_endpoint(client: HasApiHost, default_base_uri: str, path: str) -> str:
    """Prepares the full URI to send request to."""
    base_uri = client.api_host or default_base_uri
    return join_url(base_uri, path)


def format_params(params: JsonBody | None = None) -> str | None:
    """Converts request params to a JSON string for the request body."""
    return json.dumps(params) if params is not None else None


def join_url(base: str, path: str) -> str:
    """
    Safe join for base URL and path
    """
    url = base.rstrip("/") + "/" + path.lstrip("/")
    return url.rstrip("/")
