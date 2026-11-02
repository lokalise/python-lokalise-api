"""
lokalise.oauth2.request
~~~~~~~~~~~~~~~~~~~~~~~
HTTP helpers for OAuth 2.0 token operations.
"""

from typing import Any

import requests

from lokalise.request import base_headers, send
from lokalise.request_utils import join_url

BASE_URL = "https://app.lokalise.com/oauth2/"


def post(
    path: str,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send an OAuth2 POST request."""
    return send(
        "POST",
        join_url(BASE_URL, path),
        params=params,
        headers=base_headers(json_body=True),
    )