"""
Tests for the OAuthClient class
"""

import pytest
import lokalise


def test_client_arguments():
    """Checks that client can receive token, timeout values, and enable_compression
    """
    client = lokalise.OAuthClient(
        "123abc",
        connect_timeout=4,
        read_timeout=2,
        enable_compression=True)
    assert client.token == "Bearer 123abc"
    assert client.connect_timeout == 4
    assert client.read_timeout == 2
    assert client.enable_compression
    assert client.token_header == "Authorization"


@pytest.mark.vcr
def test_reset_client():
    """Checks that the client can be reset
    """
    client = lokalise.OAuthClient(
        "123abc",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True)
    assert client.connect_timeout == 5
    assert client.enable_compression

    # Run an API request so that an endpoint is lazily-loaded
    with pytest.raises(lokalise.errors.BadRequest):
        client.projects()

    client.reset_client()

    assert client.token == ''
    assert client.connect_timeout is None
    assert client.read_timeout is None
    assert not client.enable_compression
