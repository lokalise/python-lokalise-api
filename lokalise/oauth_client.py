"""
lokalise.oauth_client
~~~~~~~~~~~~~~~~~~~~~
This module contains API client that can be used with OAuth 2 tokens.
"""

from .client import Client


class OAuthClient(Client):
    """Client used to send API requests with OAuth 2 tokens.

    Usage:

        import lokalise
        client = lokalise.OAuthClient('oauth2_api_token')
        client.projects()
    """

    def __init__(
        self,
        token: str,
        connect_timeout: int | float | None = None,
        read_timeout: int | float | None = None,
        enable_compression: bool | None = False,
        api_host: str | None = None,
    ) -> None:
        """Instantiate a new Lokalise API client with OAuth 2 token.

        :param str token: Your Lokalise API token obtained via OAuth 2 flow.
        :param connect_timeout: (optional) Server connection timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type connect_timeout: int or float
        :param read_timeout: (optional) Server read timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type read_timeout: int or float
        :param enable_compression: (optional) Whether to enable gzip compression.
        :param api_host: (optional) Custom API host to send requests to.
        By default it's off.
        :type enable_compression: bool
        """
        super().__init__(token, connect_timeout, read_timeout, enable_compression, api_host)

        self._token = f"Bearer {token}"
        self._token_header = "Authorization"
