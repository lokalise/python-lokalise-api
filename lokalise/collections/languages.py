"""
lokalise.collections.languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing languages collection.
"""

from ..models.language import LanguageModel
from .base_collection import BaseCollection


class LanguagesCollection(BaseCollection[LanguageModel]):
    """Describes system and project languages."""

    DATA_KEY = "languages"
    MODEL_KLASS = LanguageModel
