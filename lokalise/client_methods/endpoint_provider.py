"""
lokalise.client_methods.endpoint_provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A simple mixin with a shared protocol.
"""

from typing import Any, Protocol


class EndpointProviderMixin(Protocol):
    """Protocol to indicate the class provides `get_endpoint`."""

    def get_endpoint(self, name: str) -> Any:
        """This method should be defined in the parent class that collects all client methods."""
