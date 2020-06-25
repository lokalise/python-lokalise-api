"""
lokalise.collections.translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translations collection.
"""

from .base_collection import BaseCollection
from ..models.translation import TranslationModel


class TranslationsCollection(BaseCollection):
    """Describes translations.
    """
    DATA_KEY = "translations"
    MODEL_KLASS = TranslationModel
