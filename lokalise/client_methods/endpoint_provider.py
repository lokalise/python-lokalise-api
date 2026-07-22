"""
lokalise.client_methods.endpoint_provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A simple mixin with a shared protocol.
"""

from typing import Any, Protocol


class EndpointProviderMixin(Protocol):
    """Protocol for classes that provide endpoint loading."""

    def get_endpoint(
        self,
        name: str,
        namespace: str | None = None,
    ) -> Any:
        """Load an endpoint from the root or an optional nested namespace."""
