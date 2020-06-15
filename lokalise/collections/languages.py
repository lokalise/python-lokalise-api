"""
lokalise.collections.languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing languages collection.
"""

from .base_collection import BaseCollection
from ..models.language import LanguageModel


class LanguagesCollection(BaseCollection):
    """Describes system and project languages.
    """
    DATA_KEY = "languages"
    MODEL_KLASS = LanguageModel
