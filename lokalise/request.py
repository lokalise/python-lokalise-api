"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.
"""

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


def get(client, path, params={}):
    return respond_with(requests.get(BASE_URL + path,
                                     params=params,
                                     **options(client)))


def respond_with(response):
    data = response.json()

    if response.status_code > 399 or "error" in data:
        respond_with_error(data, response.status_code)

    return {**data, **extract_headers_from(response)}


def respond_with_error(data, code):
    msg = data['error']['message']
    if code in errors.ERROR_CODES:
        raise errors.ERROR_CODES[code](msg, code)

    raise errors.ClientError(msg, code)


def extract_headers_from(response):
    return {
        "_pagination": {
            k.lower(): v for k,
            v in response.headers.items() if k.lower() in PAGINATION_HEADERS}}


def options(client):
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
        "X-Api-Token": client.token,
    }
    return {
        "timeout": (client.connect_timeout, client.read_timeout),
        "headers": headers
    }
