
"""
lokalise.client_vantage
~~~~~~~~~~~~~~~~~~~~~~~
This module contains the Lokalise Vantage API client definition.
"""

from .base_client import BaseClient
from .types import Number

BASE_URL_VANTAGE = "https://api.lokalise.com/vantage/v1/"


class ClientVantage(BaseClient):
    """Client used to send Lokalise Vantage API requests."""

    def __init__(
        self,
        token: str,
        connect_timeout: Number | None = None,
        read_timeout: Number | None = None,
        enable_compression: bool = False,
        api_host: str | None = None,
    ) -> None:
        """Create a new Lokalise Vantage API client instance.

        Args:
            token: Your Lokalise API token (non-empty string).
            connect_timeout: Optional connection timeout in seconds.
            read_timeout: Optional read timeout in seconds.
            enable_compression: Whether to enable gzip compression.
            api_host: Optional custom API host. Defaults to the
                official Lokalise Vantage API.
        """
        super().__init__(
            token=token,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            enable_compression=enable_compression,
            api_host=api_host,
        )

        if self.api_host is None:
            self.api_host = BASE_URL_VANTAGE
