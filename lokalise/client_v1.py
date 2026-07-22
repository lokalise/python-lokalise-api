"""
lokalise.client_v1
~~~~~~~~~~~~~~~~~~
This module contains the base Lokalise API client definition.
"""

from .base_client import BaseClient
from .client_methods.v1.audit_logs import AuditLogsMethods

Number = int | float


BASE_URL_V1 = "https://api.lokalise.com/v1/"


class ClientV1(BaseClient, AuditLogsMethods):
    """ClientV1 used to configure and send Lokalise API requests to new endpoint."""

    def __init__(
        self,
        token: str,
        connect_timeout: Number | None = None,
        read_timeout: Number | None = None,
        enable_compression: bool = False,
        api_host: str | None = None,
    ) -> None:
        """Create a new Lokalise API client v1 instance.

        Args:
            token: Your Lokalise API token (non-empty string).
            connect_timeout: Optional connection timeout in seconds. ``None`` means
                wait indefinitely.
            read_timeout: Optional read timeout in seconds. ``None`` means
                wait indefinitely.
            enable_compression: Whether to enable gzip compression (default: False).
            api_host: Optional custom API host. Defaults to the official Lokalise API.
        """

        super().__init__(token, connect_timeout, read_timeout, enable_compression, api_host)

        if self._api_host is None:
            self._api_host = BASE_URL_V1
