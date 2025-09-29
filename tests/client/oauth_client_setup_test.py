"""
Tests for the OAuthClient class
"""

from lokalise import OAuthClient


def test_client_arguments(oauth_client: OAuthClient) -> None:
    """Checks that client can receive token, timeout values, and enable_compression"""
    token = oauth_client.token
    assert token is not None, "OAuthClient.token must not be None"
    assert "Bearer" in token

    assert oauth_client.connect_timeout == 4
    assert oauth_client.read_timeout == 2
    assert oauth_client.enable_compression
    assert oauth_client.token_header == "Authorization"


def test_reset_client(oauth_client: OAuthClient) -> None:
    """Checks that the client can be reset"""
    assert oauth_client.connect_timeout == 4

    oauth_client.reset_client()

    assert oauth_client.token is None
