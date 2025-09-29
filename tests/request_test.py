"""
Tests for the request methods
"""

import lokalise
from lokalise.request import BASE_URL, options, path_to_endpoint


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
