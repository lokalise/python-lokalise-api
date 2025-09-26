from typing import Any

from lokalise.models.base_model import BaseModel

class SegmentModel(BaseModel):
    segment_number: int
    language_iso: str
    modified_at: str
    modified_at_timestamp: int
    modified_by: int
    modified_by_email: str
    value: str
    is_fuzzy: bool
    is_reviewed: bool
    reviewed_by: int
    words: int
    custom_translation_statuses: list[dict[str, Any]]
