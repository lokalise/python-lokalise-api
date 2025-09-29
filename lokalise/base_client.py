"""
lokalise.base_client
~~~~~~~~~~~~~~~~~~~~
This module contains the base Lokalise API client definition.
"""

from .types import FullClientProto

Number = int | float


class BaseClient(FullClientProto):
    """Base client used to configure and send Lokalise API requests."""

    def __init__(
        self,
        token: str,
        connect_timeout: Number | None = None,
        read_timeout: Number | None = None,
        enable_compression: bool = False,
        api_host: str | None = None,
    ) -> None:
        """Create a new Lokalise API client instance.

        Args:
            token: Your Lokalise API token (non-empty string).
            connect_timeout: Optional connection timeout in seconds. ``None`` means
                wait indefinitely.
            read_timeout: Optional read timeout in seconds. ``None`` means
                wait indefinitely.
            enable_compression: Whether to enable gzip compression (default: False).
            api_host: Optional custom API host. Defaults to the official Lokalise API.
        """
        if not token:
            raise ValueError("token must be a non-empty string")

        self._token: str | None = token
        self._connect_timeout: Number | None = connect_timeout
        self._read_timeout: Number | None = read_timeout
        self._enable_compression: bool = bool(enable_compression)
        self._api_host: str | None = api_host.strip() if api_host and api_host.strip() else None
        self._token_header: str = "X-Api-Token"

    # ---------------------------------------------------------------------
    # Properties
    # ---------------------------------------------------------------------

    @property
    def token(self) -> str | None:
        """Return the current API token, or None if not set."""
        return self._token

    @token.setter
    def token(self, value: str | None) -> None:
        if not value:
            raise ValueError("token must be a non-empty string")
        self._token = value

    @property
    def connect_timeout(self) -> Number | None:
        """Connection timeout in seconds, or ``None`` for no limit."""
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, value: Number | None) -> None:
        if value is not None and value < 0:
            raise ValueError("connect_timeout must be non-negative or None")
        self._connect_timeout = value

    @property
    def read_timeout(self) -> Number | None:
        """Read timeout in seconds, or ``None`` for no limit."""
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, value: Number | None) -> None:
        if value is not None and value < 0:
            raise ValueError("read_timeout must be non-negative or None")
        self._read_timeout = value

    @property
    def enable_compression(self) -> bool:
        """Whether gzip compression is enabled."""
        return self._enable_compression

    @enable_compression.setter
    def enable_compression(self, value: bool | None) -> None:
        self._enable_compression = bool(value)

    @property
    def api_host(self) -> str | None:
        """Custom API host, or ``None`` to use the default Lokalise API."""
        return self._api_host

    @api_host.setter
    def api_host(self, value: str | None) -> None:
        self._api_host = value.strip() if value and value.strip() else None

    @property
    def token_header(self) -> str:
        """HTTP header key used for the API token."""
        return self._token_header
