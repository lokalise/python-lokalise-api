"""
lokalise.endpoints.segments_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing segments endpoint.
"""

from .base_endpoint import BaseEndpoint


class SegmentsEndpoint(BaseEndpoint):
    """Describes segments endpoint."""

    PATH = "projects/$parent_id/keys/$resource_id/segments/$subresource_id"
