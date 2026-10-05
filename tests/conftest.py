"""
Contains fixture functions for the tests.
"""

import os
from pathlib import Path
from types import ModuleType
from typing import Any, Protocol, cast

import lokalise
import pytest
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


FILTERED_RESPONSE_HEADERS = {
    "set-cookie",
    "date",
    "expires",
    "x-lokalise-process-id",
    "x-ratelimit-remaining",
    "x-ratelimit-reset",
}


class _ReqWithModule(Protocol):
    module: ModuleType | None


def scrub_response_headers(response: dict[str, Any]) -> dict[str, Any]:
    """Remove sensitive headers before saving a response to a cassette."""
    headers = response.get("headers")

    if not isinstance(headers, dict):
        return response

    typed_headers = cast(dict[str, Any], headers)

    for header_name in list(typed_headers):
        if header_name.lower() in FILTERED_RESPONSE_HEADERS:
            typed_headers.pop(header_name)

    return response


@pytest.fixture(scope="module")
def vcr_config() -> dict[str, Any]:
    """Configuration for the VCR module."""
    return {
        "filter_headers": [
            ("x-api-token", "FILTERED"),
            ("Authorization", "FILTERED"),
        ],
        "filter_post_data_parameters": [
            "client_secret",
            "client_id",
            "refresh_token",
            "code",
        ],
        "before_record_response": scrub_response_headers,
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
    path = Path("tests/fixtures/screenshot_base64.txt")

    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


@pytest.fixture
def client() -> lokalise.Client:
    token = os.getenv("LOKALISE_API_TOKEN") or "DUMMY_API_TOKEN"
    return lokalise.Client(token)


@pytest.fixture
def clientv1() -> lokalise.ClientV1:
    token = os.getenv("LOKALISE_API_TOKEN") or "DUMMY_API_TOKEN"
    return lokalise.ClientV1(token)


@pytest.fixture
def oauth_client() -> lokalise.OAuthClient:
    token = os.getenv("OAUTH2_TOKEN") or "DUMMY_OAUTH2_TOKEN"
    return lokalise.OAuthClient(
        token,
        connect_timeout=4,
        read_timeout=2,
        enable_compression=True,
    )


@pytest.fixture
def auth_client() -> lokalise.Auth:
    client_id = os.getenv("OAUTH2_CLIENT_ID") or "DUMMY_OAUTH2_CLIENT_ID"
    client_secret = os.getenv("OAUTH2_CLIENT_SECRET") or "DUMMY_OAUTH2_CLIENT_SECRET"

    return lokalise.Auth(client_id, client_secret)
