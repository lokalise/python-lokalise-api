"""
lokalise.collections.translation_memories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation memories collection.
"""

from ..models.translation_memory import TranslationMemoryModel
from .expert_collection import ExpertCollection


class TranslationMemoriesCollection(ExpertCollection[TranslationMemoryModel]):
    """Describes translation memories."""

    DATA_KEY = "translation_memories"
    MODEL_KLASS = TranslationMemoryModel
