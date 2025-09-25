"""
lokalise.endpoints.languages_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing project languages endpoint.
"""

from .base_endpoint import BaseEndpoint


class LanguagesEndpoint(BaseEndpoint):
    """Describes project languages endpoint."""

    PATH = "projects/$parent_id/languages/$resource_id"
