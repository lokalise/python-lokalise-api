"""
lokalise.base_client
~~~~~~~~~~~~~~~~~~~~
This module contains base API client definition.
"""

from .types import FullClientProto

Number = int | float


class BaseClient(FullClientProto):
    """Base client used to send API requests."""

    def __init__(
        self,
        token: str,
        connect_timeout: int | float | None = None,
        read_timeout: int | float | None = None,
        enable_compression: bool | None = False,
        api_host: str | None = None,
    ) -> None:
        """Instantiate a new Lokalise API client.

        :param str token: Your Lokalise API token.
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
        self._token = token
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        self._enable_compression = enable_compression
        self._api_host = api_host
        self._token_header = "X-Api-Token"

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, value: str) -> None:
        if not value:
            raise ValueError("token must be a non-empty string")
        self._token = value

    @property
    def connect_timeout(self) -> Number | None:
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, value: Number | None) -> None:
        if value is not None and value < 0:
            raise ValueError("connect_timeout must be a non-negative number or None")
        self._connect_timeout = value

    @property
    def read_timeout(self) -> Number | None:
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, value: Number | None) -> None:
        if value is not None and value < 0:
            raise ValueError("read_timeout must be a non-negative number or None")
        self._read_timeout = value

    @property
    def enable_compression(self) -> bool | None:
        return self._enable_compression

    @enable_compression.setter
    def enable_compression(self, value: bool | None) -> None:
        self._enable_compression = bool(value) if value is not None else False

    @property
    def api_host(self) -> str | None:
        return self._api_host

    @api_host.setter
    def api_host(self, value: str | None) -> None:
        if value is not None:
            v = value.strip()
            if not v:
                value = None
        self._api_host = value

    @property
    def token_header(self) -> str:
        return self._token_header
