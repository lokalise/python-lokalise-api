"""
lokalise.oauth2.request
~~~~~~~~~~~~~~~~~~~~~~~
HTTP helpers specifically for OAuth 2.0 flow.
"""

from typing import Any

import requests

from lokalise._version import __version__
from lokalise.request_utils import format_params, join_url, raise_on_error

BASE_URL = "https://app.lokalise.com/oauth2/"


def post(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    Perform an OAuth2 POST request (token exchange/revoke/etc).
    Returns parsed JSON or raises a structured error.
    """
    url = join_url(BASE_URL, path)
    resp = requests.post(url, data=format_params(params), **options())
    return respond_with(resp)


def respond_with(response: requests.Response) -> dict[str, Any]:
    """
    Parse JSON body and raise on HTTP error or on payload containing 'error'.
    """
    try:
        data: dict[str, Any] = response.json()
    except ValueError:
        data = {"_raw_body": response.text}
    raise_on_error(response, data)
    return data


def options() -> dict[str, Any]:
    """
    Minimal headers for OAuth endpoints. No auth header here.
    """
    headers: dict[str, Any] = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
        "Content-Type": "application/json",
    }
    return {"headers": headers}
