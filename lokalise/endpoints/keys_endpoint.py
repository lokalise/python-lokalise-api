"""
lokalise.endpoints.keys_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing keys endpoint.
"""
from .base_endpoint import BaseEndpoint


class KeysEndpoint(BaseEndpoint):
    """Describes keys endpoint.
    """
    PATH = "projects/$parent_id/keys/$resource_id"
