"""
lokalise.endpoints.jwt_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing JWT endpoint.
"""

from .base_endpoint import BaseEndpoint


class JwtEndpoint(BaseEndpoint):
    """Describes JWT endpoint."""

    PATH = "projects/$parent_id/tokens"
