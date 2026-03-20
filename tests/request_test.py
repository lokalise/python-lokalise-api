"""
Tests for the request methods
"""

from unittest.mock import Mock, patch

import lokalise
import pytest
from lokalise.request import BASE_URL, options, path_to_endpoint, respond_with
from lokalise.request_utils import respond_with_error


def test_options_with_api_client():
    """Checks that client can receive token, timeout values, and enable_compression"""
    client = lokalise.Client("123abc", connect_timeout=5, read_timeout=3, enable_compression=True)

    opts = options(client)

    assert opts["headers"]["X-Api-Token"] == "123abc"
    assert "Authorization" not in opts["headers"]
    assert opts["headers"]["Accept-Encoding"] == "gzip,deflate,br"
    assert opts["timeout"] == (5, 3)


def test_path_to_endpoint_with_api_client():
    """Checks that the API host can be overridden"""
    client = lokalise.Client("123abc", connect_timeout=5, read_timeout=3, enable_compression=True)

    full_path = path_to_endpoint(client, BASE_URL, "projects")

    assert full_path == BASE_URL + "projects"

    custom_api_host = "http://example.com/api/"
    customized_client = lokalise.Client(
        "123abc",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True,
        api_host=custom_api_host,
    )

    full_path = path_to_endpoint(customized_client, BASE_URL, "projects")

    assert full_path == custom_api_host + "projects"


def test_path_to_endpoint_with_oauth_api_client():
    """Checks that the API host can be overridden for OAuth2 client"""
    client = lokalise.OAuthClient(
        "345xyz", connect_timeout=5, read_timeout=3, enable_compression=True
    )

    full_path = path_to_endpoint(client, BASE_URL, "projects")

    assert full_path == BASE_URL + "projects"

    custom_api_host = "http://example.com/api/"
    customized_client = lokalise.OAuthClient(
        "345xyz",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True,
        api_host=custom_api_host,
    )

    full_path = path_to_endpoint(customized_client, BASE_URL, "projects")

    assert full_path == custom_api_host + "projects"


def test_options_with_oauth_api_client():
    """Checks that client can receive token, timeout values, and enable_compression"""
    client = lokalise.OAuthClient(
        "345xyz", connect_timeout=5, read_timeout=3, enable_compression=True
    )

    opts = options(client)

    assert opts["headers"]["Authorization"] == "Bearer 345xyz"
    assert "X-Api-Token" not in opts["headers"]
    assert opts["headers"]["Accept-Encoding"] == "gzip,deflate,br"
    assert opts["timeout"] == (5, 3)


def test_respond_with_uses_raw_body_when_json_is_invalid():
    response = Mock()
    response.json.side_effect = ValueError
    response.text = "not json"
    response.headers = {}

    with patch("lokalise.request.raise_on_error"):
        result = respond_with(response)

    assert result["_raw_body"] == "not json"


def test_options_raises_after_client_reset():
    """Checks that options() raises after client.reset_client()"""
    client = lokalise.Client("123abc")
    client.reset_client()

    with pytest.raises(RuntimeError, match=r"API token is not set"):
        options(client)


def test_respond_with_error_uses_raw_body_when_present():
    """Checks that _raw_body is used when present in data"""
    with patch("lokalise.request_utils.errors.error_from_http") as error_from_http:
        error_from_http.side_effect = RuntimeError("boom")

        with pytest.raises(RuntimeError, match="boom"):
            respond_with_error({"_raw_body": "raw error text"}, 400)

        error_from_http.assert_called_once_with(
            400,
            message=None,
            headers=None,
            body_text="raw error text",
        )
