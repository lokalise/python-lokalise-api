
"""
Tests for HTTP request methods.
"""

from unittest.mock import Mock, PropertyMock, patch
from requests import Response
import pytest

import lokalise

from lokalise.request import BASE_URL, get, options
from lokalise.request_utils import path_to_endpoint


def test_options_with_api_client():
    """Check API token, timeout values, and compression."""
    client = lokalise.Client(
        "123abc",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True,
    )

    opts = options(client)

    assert opts["headers"]["X-Api-Token"] == "123abc"
    assert "Authorization" not in opts["headers"]
    assert opts["headers"]["Accept-Encoding"] == "gzip,deflate"
    assert opts["timeout"] == (5, 3)


def test_path_to_endpoint_with_api_client():
    """Check that the API host can be overridden."""
    client = lokalise.Client("123abc")

    full_path = path_to_endpoint(client, BASE_URL, "projects")

    assert full_path == BASE_URL + "projects"

    custom_api_host = "http://example.com/api/"
    customized_client = lokalise.Client(
        "123abc",
        api_host=custom_api_host,
    )

    full_path = path_to_endpoint(
        customized_client,
        BASE_URL,
        "projects",
    )

    assert full_path == custom_api_host + "projects"


def test_path_to_endpoint_with_oauth_api_client():
    """Check API host overrides for OAuth2 clients."""
    client = lokalise.OAuthClient("345xyz")

    full_path = path_to_endpoint(client, BASE_URL, "projects")

    assert full_path == BASE_URL + "projects"

    custom_api_host = "http://example.com/api/"
    customized_client = lokalise.OAuthClient(
        "345xyz",
        api_host=custom_api_host,
    )

    full_path = path_to_endpoint(
        customized_client,
        BASE_URL,
        "projects",
    )

    assert full_path == custom_api_host + "projects"


def test_options_with_oauth_api_client():
    """Check OAuth2 authentication and request options."""
    client = lokalise.OAuthClient(
        "345xyz",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True,
    )

    opts = options(client)

    assert opts["headers"]["Authorization"] == "Bearer 345xyz"
    assert "X-Api-Token" not in opts["headers"]
    assert opts["headers"]["Accept-Encoding"] == "gzip,deflate"
    assert opts["timeout"] == (5, 3)


def test_get_returns_raw_response() -> None:
    """Check that request.get returns an unparsed HTTP response."""
    client = lokalise.Client("123abc")
    raw_response = Mock(spec=Response)

    with patch(
        "lokalise.request.requests.request",
        return_value=raw_response,
    ) as mocked_request:
        result = get(client, "projects", {"page": 2})

    assert result is raw_response
    raw_response.json.assert_not_called()

    mocked_request.assert_called_once()

    args, kwargs = mocked_request.call_args

    assert args == ("GET", BASE_URL + "projects")
    assert kwargs["params"] == {"page": 2}
    assert kwargs["headers"]["X-Api-Token"] == "123abc"
    assert kwargs["timeout"] is None

def test_options_rejects_missing_token() -> None:
    """Check that request options cannot be built without an API token."""
    client = lokalise.Client("123abc")

    with patch.object(
        type(client),
        "token",
        new_callable=PropertyMock,
        return_value=None,
    ):
        with pytest.raises(
            RuntimeError,
            match="Cannot build headers: API token is not set",
        ):
            options(client)