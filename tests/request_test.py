"""
Tests for the request methods
"""

import lokalise
from lokalise.request import options


def test_options_with_api_client():
    """Checks that client can receive token, timeout values, and enable_compression
    """
    client = lokalise.Client(
        "123abc",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True)

    opts = options(client)

    assert opts["headers"]["X-Api-Token"] == "123abc"
    assert "Authorization" not in opts["headers"]
    assert opts["headers"]["Accept-Encoding"] == "gzip,deflate,br"
    assert opts["timeout"] == (5, 3)


def test_options_with_oauth_api_client():
    """Checks that client can receive token, timeout values, and enable_compression
    """
    client = lokalise.OAuthClient(
        "345xyz",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True)

    opts = options(client)

    assert opts["headers"]["Authorization"] == "Bearer 345xyz"
    assert "X-Api-Token" not in opts["headers"]
    assert opts["headers"]["Accept-Encoding"] == "gzip,deflate,br"
    assert opts["timeout"] == (5, 3)
