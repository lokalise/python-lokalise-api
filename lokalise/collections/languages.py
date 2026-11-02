"""
lokalise.collections.languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing languages collection.
"""

from ..models.language import LanguageModel
from .expert_collection import ExpertCollection


class LanguagesCollection(ExpertCollection[LanguageModel]):
    """Describes system and project languages."""

    DATA_KEY = "languages"
    MODEL_KLASS = LanguageModel
