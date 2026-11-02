"""
lokalise.collections.translation_statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation statuses collection.
"""

from ..models.translation_status import TranslationStatusModel
from .expert_collection import ExpertCollection


class TranslationStatusesCollection(ExpertCollection[TranslationStatusModel]):
    """Describes translation statuses."""

    DATA_KEY = "custom_translation_statuses"
    MODEL_KLASS = TranslationStatusModel
