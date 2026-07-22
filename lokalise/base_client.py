"""
lokalise.base_client
~~~~~~~~~~~~~~~~~~~~
This module contains the base Lokalise API client definition.
"""

import importlib
from collections.abc import Callable
from typing import TypeVar, cast

from lokalise.utils import snake_to_camel

from .endpoints.base_endpoint import BaseEndpoint
from .types import FullClientProto

Number = int | float

T = TypeVar("T", bound=BaseEndpoint)


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

    def reset_client(self) -> None:
        """Resets the API client by clearing all attributes.
        After reset, token is None and client is unusable until you set a new token.
        """
        self._token = None
        self._connect_timeout = None
        self._read_timeout = None
        self._enable_compression = False
        self._clear_endpoint_attrs()

    # === Endpoint helpers
    def get_endpoint(
        self,
        name: str,
        namespace: str | None = None,
    ) -> BaseEndpoint:
        """Lazily load and cache an endpoint.

        Args:
            name: Endpoint name, such as ``projects`` or ``audit_logs``.
            namespace: Optional nested endpoint package, such as ``v1``.
        """
        endpoint_name = f"{name}_endpoint"
        class_name = snake_to_camel(endpoint_name)

        module_parts = [".endpoints"]

        if namespace:
            module_parts.append(namespace)

        module_parts.append(endpoint_name)
        module_path = ".".join(module_parts)

        attr_name = f"_{namespace}_{endpoint_name}" if namespace else f"_{endpoint_name}"

        try:
            module = importlib.import_module(module_path, package="lokalise")
            endpoint_class = cast(
                type[BaseEndpoint],
                getattr(module, class_name),
            )
        except (ModuleNotFoundError, AttributeError) as exc:
            qualified_name = f"{namespace}.{name}" if namespace else name
            raise ValueError(f"Unknown endpoint: {qualified_name}") from exc

        return self._fetch_attr(
            attr_name,
            lambda: endpoint_class(self),
        )

    def _fetch_attr(self, attr_name: str, populator: Callable[[], T]) -> T:
        """Searches for the given attribute.
        Uses populator to set the attribute if it cannot be found.
        Used to lazy-load endpoints.
        """
        val = getattr(self, attr_name, None)
        if val is None:
            val = populator()
            setattr(self, attr_name, val)
        return cast(T, val)

    def _clear_endpoint_attrs(self) -> None:
        """Clears all lazily-loaded endpoint attributes"""
        for attr in [a for a in vars(self) if a.endswith("_endpoint")]:
            delattr(self, attr)
