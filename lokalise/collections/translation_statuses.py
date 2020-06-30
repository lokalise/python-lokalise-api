"""
lokalise.collections.translation_statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation statuses collection.
"""

from .base_collection import BaseCollection
from ..models.translation_status import TranslationStatusModel


class TranslationStatusesCollection(BaseCollection):
    """Describes translation statuses.
    """
    DATA_KEY = "custom_translation_statuses"
    MODEL_KLASS = TranslationStatusModel
