"""
lokalise.endpoints.translations_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translations endpoint.
"""
from .base_endpoint import BaseEndpoint


class TranslationsEndpoint(BaseEndpoint):
    """Describes translations endpoint.
    """
    PATH = "projects/$parent_id/translations/$resource_id"
