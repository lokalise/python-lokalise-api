"""
lokalise.models.language
~~~~~~~~~~~~~~~~~~~~~~~~
Module containing language model.
"""

from .base_model import BaseModel


class LanguageModel(BaseModel):
    """Describes project or system language."""

    DATA_KEY = "language"

    ATTRS = ["lang_id", "lang_iso", "lang_name", "is_rtl", "plural_forms", "project_language_uuid"]
