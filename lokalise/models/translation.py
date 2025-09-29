"""
lokalise.models.translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation model.
"""

from .base_model import BaseModel


class TranslationModel(BaseModel):
    """Describes translation model."""

    DATA_KEY = "translation"

    ATTRS = [
        "translation_id",
        "key_id",
        "language_iso",
        "modified_at",
        "modified_at_timestamp",
        "modified_by",
        "modified_by_email",
        "translation",
        "is_fuzzy",
        "is_unverified",
        "is_reviewed",
        "reviewed_by",
        "words",
        "custom_translation_statuses",
        "task_id",
        "segment_number",
    ]
