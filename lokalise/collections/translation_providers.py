"""
lokalise.collections.translation_providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation providers collection.
"""

from ..models.translation_provider import TranslationProviderModel
from .expert_collection import ExpertCollection


class TranslationProvidersCollection(ExpertCollection[TranslationProviderModel]):
    """Describes translation providers."""

    DATA_KEY = "translation_providers"
    MODEL_KLASS = TranslationProviderModel
