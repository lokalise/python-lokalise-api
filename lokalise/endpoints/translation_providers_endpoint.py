"""
lokalise.endpoints.translation_providers_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation providers endpoint.
"""

from .base_endpoint import BaseEndpoint


class TranslationProvidersEndpoint(BaseEndpoint):
    """Describes translation providers endpoint."""

    PATH = "teams/$parent_id/translation_providers/$resource_id"
