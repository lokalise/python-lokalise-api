"""
lokalise.endpoints.jwt_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing JWT endpoint.
"""
from .base_endpoint import BaseEndpoint


class JwtEndpoint(BaseEndpoint):
    """Describes JWT endpoint.
    """
    PATH = "jwt-tokens/ota"
