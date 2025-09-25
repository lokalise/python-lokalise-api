"""
lokalise.collections.translation_providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation providers collection.
"""

from ..models.translation_provider import TranslationProviderModel
from .base_collection import BaseCollection


class TranslationProvidersCollection(BaseCollection[TranslationProviderModel]):
    """Describes translation providers."""

    DATA_KEY = "translation_providers"
    MODEL_KLASS = TranslationProviderModel
