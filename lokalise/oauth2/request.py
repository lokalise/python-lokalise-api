"""
lokalise.oauth2.request
~~~~~~~~~~~~~~~~~~~~~~~
HTTP helpers specifically for OAuth 2.0 flow.
"""

from typing import Any, Optional
import requests

from lokalise._version import __version__
from lokalise.request_utils import raise_on_error, format_params

BASE_URL = "https://app.lokalise.com/oauth2/"


def post(path: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    """
    Perform an OAuth2 POST request (token exchange/revoke/etc).
    Returns parsed JSON or raises a structured error.
    """
    url = __join_url(BASE_URL, path)
    resp = requests.post(url, data=format_params(params), **options())
    return respond_with(resp)


def respond_with(response: requests.Response) -> dict[str, Any]:
    """
    Parse JSON body and raise on HTTP error or on payload containing 'error'.
    """
    data: dict[str, Any] = response.json()
    raise_on_error(response, data)
    return data


def options() -> dict[str, Any]:
    """
    Minimal headers for OAuth endpoints. No auth header here.
    """
    headers: dict[str, Any] = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
    }
    return {"headers": headers}


def __join_url(base: str, path: str) -> str:
    """
    Safe join for base URL and path
    """
    url = base.rstrip("/") + "/" + path.lstrip("/")
    return url.rstrip("/")
