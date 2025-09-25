"""
lokalise.collections.translation_statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation statuses collection.
"""

from ..models.translation_status import TranslationStatusModel
from .base_collection import BaseCollection


class TranslationStatusesCollection(BaseCollection[TranslationStatusModel]):
    """Describes translation statuses."""

    DATA_KEY = "custom_translation_statuses"
    MODEL_KLASS = TranslationStatusModel
