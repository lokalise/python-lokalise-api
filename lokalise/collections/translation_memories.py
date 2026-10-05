"""
lokalise.collections.translation_memories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation memories collection.
"""

from ..models.translation_memory import TranslationMemoryModel
from .base_collection import BaseCollection


class TranslationMemoriesCollection(BaseCollection[TranslationMemoryModel]):
    """Describes translation memories."""

    DATA_KEY = "translation_memories"
    MODEL_KLASS = TranslationMemoryModel
