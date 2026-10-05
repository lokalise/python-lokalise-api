"""
lokalise.endpoints.translation_memories_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation memories endpoint.
"""

from .base_endpoint import BaseEndpoint


class TranslationMemoriesEndpoint(BaseEndpoint):
    """Describes translation memories endpoint."""

    PATH = "projects/$parent_id/translation-memories"
