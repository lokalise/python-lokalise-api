"""
lokalise.models.segment
~~~~~~~~~~~~~~~~~~~~~~~
Module containing segment model.
"""

from .base_model import BaseModel


class SegmentModel(BaseModel):
    """Describes segment."""

    DATA_KEY = "segment"

    ATTRS = [
        "segment_number",
        "language_iso",
        "modified_at",
        "modified_at_timestamp",
        "modified_by",
        "modified_by_email",
        "value",
        "is_fuzzy",
        "is_reviewed",
        "reviewed_by",
        "words",
        "custom_translation_statuses",
    ]
