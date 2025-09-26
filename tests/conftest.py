"""
Contains fixture functions for the tests.
"""

import os
from types import ModuleType
from typing import Protocol

import lokalise
import pytest
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class _ReqWithModule(Protocol):
    module: ModuleType | None


@pytest.fixture(scope="module")
def vcr_config():
    """Configuration for the VCR module"""
    return {
        "filter_headers": [("x-api-token", "FILTERED"), ("Authorization", "FILTERED")],
        "filter_post_data_parameters": ["client_secret", "client_id", "refresh_token"],
        "decode_compressed_response": True,
    }


@pytest.fixture(scope="module")
def vcr_cassette_dir(request: _ReqWithModule) -> str:
    """Sets the path to save cassettes to."""
    module = request.module
    mod_name = module.__name__ if module is not None else "unknown"
    mod_path = mod_name.replace(".", os.sep)
    return os.path.join("tests", "cassettes", mod_path)


@pytest.fixture(scope="module")
def screenshot_data() -> str:
    """Loads base64-encoded screenshot data."""
    try:
        path = "tests/fixtures/screenshot_base64.txt"
        with open(os.path.join(path), encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        return ""
    file.close()
    return data


@pytest.fixture(scope="module")
def client() -> lokalise.Client:
    """Creates a sample client object using the token from the ENV."""
    token = os.getenv("LOKALISE_API_TOKEN") or "DUMMY_API_TOKEN"
    return lokalise.Client(token)


@pytest.fixture(scope="module")
def oauth_client() -> lokalise.OAuthClient:
    """Creates a sample client object using the OAuth token from the ENV."""
    token = os.getenv("OAUTH2_TOKEN") or "DUMMY_OAUTH2_TOKEN"
    return lokalise.OAuthClient(token, connect_timeout=4, read_timeout=2, enable_compression=True)


@pytest.fixture(scope="module")
def auth_client():
    """Create a sample client object to manage OAuth 2 tokens."""
    client_id = os.getenv("OAUTH2_CLIENT_ID") or "DUMMY_OAUTH2_CLIENT_ID"
    client_secret = os.getenv("OAUTH2_CLIENT_SECRET") or "DUMMY_OAUTH2_CLIENT_SECRET"
    return lokalise.Auth(client_id, client_secret)
