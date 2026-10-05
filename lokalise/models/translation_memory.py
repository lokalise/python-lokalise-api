"""
lokalise.models.translation_memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation memory model.
"""

from .base_model import BaseModel


class TranslationMemoryModel(BaseModel):
    """Describes translation memory."""

    DATA_KEY = "translation_memory"

    ATTRS = ("id", "name")
