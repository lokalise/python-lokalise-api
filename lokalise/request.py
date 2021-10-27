"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.

Attributes:

    :attribute str BASE_URL: path to the Lokalise APIv2.
    :attribute list PAGINATION_HEADERS: list of response headers that contain pagination data.
"""
from typing import Any, Optional, Dict, NoReturn
import json
import requests
from lokalise import errors
import lokalise.client
from ._version import __version__


BASE_URL = "https://api.lokalise.com/api2/"
PAGINATION_HEADERS = [
    "x-pagination-total-count",
    "x-pagination-page-count",
    "x-pagination-limit",
    "x-pagination-page"
]


def get(client: lokalise.client.Client, path: str,
        params: Optional[Dict] = None) -> Dict:
    """Performs GET requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.get(__prepare(BASE_URL + path),
                                     params=params,
                                     **options(client)))


def post(client: lokalise.client.Client, path: str,
         params: Optional[Dict] = None) -> Dict:
    """Performs POST requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.post(__prepare(BASE_URL + path),
                                      data=__format_params(params),
                                      **options(client)))


def put(client: lokalise.client.Client, path: str,
        params: Optional[Dict] = None) -> Dict:
    """Performs PUT requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.put(__prepare(BASE_URL + path),
                                     data=__format_params(params),
                                     **options(client)))


def patch(client: lokalise.client.Client, path: str,
          params: Optional[Dict] = None) -> Dict:
    """Performs PATCH requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.patch(__prepare(BASE_URL + path),
                                       data=__format_params(params),
                                       **options(client)))


def delete(client: lokalise.client.Client, path: str,
           params: Optional[Dict] = None) -> Dict:
    """Performs DELETE requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.delete(__prepare(BASE_URL + path),
                                        data=__format_params(params),
                                        ** options(client)))


def respond_with(response: requests.models.Response) -> Dict:
    """Converts the response data to JSON and attaches pagination-related data.
    An exception will be raised if the response status code is 4xx or 5xx,
    or contains an "error" key

    :param response: Response from the API
    :rtype dict:
    """
    data = response.json()

    if response.status_code > 399 or 'error' in data:
        respond_with_error(data, response.status_code)

    return {**data, **extract_headers_from(response)}


def respond_with_error(data: Dict[str, Any], code: Any) -> NoReturn:
    """Raises an error based on the HTTP status code.
    If the status code is unknown, raises a generic ClientError

    :param data: Response body from the API that usually contains error message
    :param code: Response status code
    """
    msg: str = ''
    if 'error' in data:
        msg = data['error']['message']
    else:
        msg = data['message']

    if code in errors.ERROR_CODES:
        raise errors.ERROR_CODES[code](msg, code)

    raise errors.ClientError(msg, code)


def extract_headers_from(response: requests.models.Response) -> Dict:
    """Fetches pagination-related data from the response headers

    :param response: Response from the API
    :rtype dict:
    """
    return {
        "_pagination": {
            k.lower(): v for k,
            v in response.headers.items() if k.lower() in PAGINATION_HEADERS
        }
    }


def options(client: lokalise.client.Client) -> Dict:
    """Prepares proper request options, including Accept headers, API token,
    and timeouts.

    :param client: Lokalise API client
    :type client: lokalise.Client
    :rtype dict:
    """
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
        "Accept-Encoding": None
    }

    headers[client.token_header] = client.token

    if client.enable_compression:
        headers["Accept-Encoding"] = "gzip,deflate,br"

    return {
        "timeout": (client.connect_timeout, client.read_timeout),
        "headers": headers
    }


def __format_params(params: Optional[Dict] = None) -> Optional[str]:
    """Converts request params to JSON
    """
    return json.dumps(params) if params else None


def __prepare(path: str) -> str:
    """Prepares the URI by stripping all unnecessary slashes
    """
    return path.strip('/')
