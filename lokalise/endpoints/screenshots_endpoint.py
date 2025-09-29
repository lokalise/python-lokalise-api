"""
lokalise.endpoints.screenshots_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing screenshots endpoint.
"""

from .base_endpoint import BaseEndpoint


class ScreenshotsEndpoint(BaseEndpoint):
    """Describes screenshots endpoint."""

    PATH = "projects/$parent_id/screenshots/$resource_id"
