# -*- coding: utf-8 -*-

"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.
"""

from ._version import __version__
import requests

BASE_URL = "https://api.lokalise.com/api2/"
PAGINATION_HEADERS = [
    "x-pagination-total-count",
    "x-pagination-page-count",
    "x-pagination-limit",
    "x-pagination-page",
]


def get(client, path):
    r = respond_with(requests.get(BASE_URL + path, **params(client)))
    print(r)


def respond_with(response):
    data = response.json()
    return {**data, **extract_headers_from(response)}


def extract_headers_from(response):
    return {
        k: v for k, v in response.headers.items() if k.lower() in PAGINATION_HEADERS
    }


def params(client):
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-lokalise-api plugin/{__version__}",
        "X-Api-Token": client.token,
    }
    return {"headers": headers}
