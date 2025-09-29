"""
lokalise.endpoints.contributors_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing contributors endpoint.
"""

from .base_endpoint import BaseEndpoint


class ContributorsEndpoint(BaseEndpoint):
    """Describes project contributors endpoint."""

    PATH = "projects/$parent_id/contributors/$resource_id"
