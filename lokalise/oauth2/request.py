"""
lokalise.oauth2.request
~~~~~~~~~~~~~~~~~~~~~~~
This module provides HTTP request methods specifically for OAuth 2 flow.
"""

import requests
from typing import Optional, Dict
from lokalise.request_utils import raise_on_error, __format_params, __prepare
from lokalise._version import __version__

BASE_URL = "https://app.lokalise.com/oauth2/"


def post(path: str,
         params: Optional[Dict] = None) -> Dict:
    """Performs POST requests

    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.post(__prepare(BASE_URL + path),
                                      data=__format_params(params),
                                      **options()))


def respond_with(response: requests.models.Response) -> Dict:
    """Converts the response data to JSON.
    An exception will be raised if the response status code is 4xx or 5xx,
    or contains an "error" key

    :param response: Response from the API
    :rtype dict:
    """
    data = response.json()
    raise_on_error(response, data)

    return data


def options() -> Dict:
    """Prepares proper request options.

    :rtype dict:
    """
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}"
    }

    return {
        "headers": headers
    }
