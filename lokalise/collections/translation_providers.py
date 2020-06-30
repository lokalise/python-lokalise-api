"""
lokalise.collections.translation_providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation providers collection.
"""

from .base_collection import BaseCollection
from ..models.translation_provider import TranslationProviderModel


class TranslationProvidersCollection(BaseCollection):
    """Describes translation providers.
    """
    DATA_KEY = "translation_providers"
    MODEL_KLASS = TranslationProviderModel
