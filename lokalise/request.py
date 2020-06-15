"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.

Attributes:

    BASE_URL - path to the Lokalise APIv2.
    PAGINATION_HEADERS - list of response headers that contain pagination data.
"""

import json
import requests
from lokalise import errors
from ._version import __version__


BASE_URL = "https://api.lokalise.com/api2/"
PAGINATION_HEADERS = [
    "x-pagination-total-count",
    "x-pagination-page-count",
    "x-pagination-limit",
    "x-pagination-page"
]


def get(client, path, params=None):
    """Performs GET requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.get(BASE_URL + path,
                                     params=params,
                                     **options(client)))


def post(client, path, params=None):
    """Performs POST requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.post(BASE_URL + path,
                                      data=format_params(params),
                                      **options(client)))


def put(client, path, params=None):
    """Performs PUT requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.put(BASE_URL + path,
                                     data=format_params(params),
                                     **options(client)))


def delete(client, path):
    """Performs DELETE requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :rtype dict:
    """
    return respond_with(requests.delete(BASE_URL + path,
                                        **options(client)))


def respond_with(response):
    """Converts the response data to JSON.
    An exception will be raised if the response status code is 4xx or 5xx,
    or contains an "error" key

    :param response: Response from the API
    :rtype dict:
    """
    data = response.json()

    if response.status_code > 399 or "error" in data:
        respond_with_error(data, response.status_code)

    return {**data, **extract_headers_from(response)}


def respond_with_error(data, code):
    """Raises an error based on the HTTP status code.
    If the status code is unknown, raises a generic ClientError

    :param data: Response body from the API that usually contains error message
    :param code: Response status code
    """
    msg = data['error']['message']
    if code in errors.ERROR_CODES:
        raise errors.ERROR_CODES[code](msg, code)

    raise errors.ClientError(msg, code)


def extract_headers_from(response):
    """Fetches pagination-related data from the response headers

    :param response: Response from the API
    :rtype dict:
    """
    return {
        "_pagination": {
            k.lower(): v for k,
            v in response.headers.items() if k.lower() in PAGINATION_HEADERS}}


def options(client):
    """Prepares proper request options, including Accept headers, API token,
    and timeouts.

    :param client: Lokalise API client
    :type client: lokalise.Client
    :rtype dict:
    """
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
        "X-Api-Token": client.token,
    }
    return {
        "timeout": (client.connect_timeout, client.read_timeout),
        "headers": headers
    }


def format_params(params):
    """Converts request params to JSON
    """
    return json.dumps(params) if params else None
