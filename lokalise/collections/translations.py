"""
lokalise.collections.translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translations collection.
"""

from ..models.translation import TranslationModel
from .expert_collection import ExpertCollection


class TranslationsCollection(ExpertCollection[TranslationModel]):
    """Describes translations."""

    DATA_KEY = "translations"
    MODEL_KLASS = TranslationModel
