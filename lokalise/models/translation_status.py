"""
lokalise.models.translation_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation status model.
"""

from .base_model import BaseModel


class TranslationStatusModel(BaseModel):
    """Describes translation status model.
    """
    DATA_KEY = "custom_translation_status"

    ATTRS = [
        "status_id",
        "title",
        "color"
    ]
