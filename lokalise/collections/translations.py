"""
lokalise.collections.translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translations collection.
"""

from ..models.translation import TranslationModel
from .base_collection import BaseCollection


class TranslationsCollection(BaseCollection[TranslationModel]):
    """Describes translations."""

    DATA_KEY = "translations"
    MODEL_KLASS = TranslationModel
