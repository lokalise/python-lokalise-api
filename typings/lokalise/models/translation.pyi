from typing import TypedDict

from lokalise.models.base_model import BaseModel

class TranslationStatus(TypedDict):
    status_id: int
    title: str
    color: str

class TranslationModel(BaseModel):
    translation_id: int
    key_id: int
    language_iso: str
    modified_at: str
    modified_at_timestamp: int
    modified_by: int
    modified_by_email: str
    translation: str
    is_unverified: bool
    is_reviewed: bool
    is_fuzzy: bool
    reviewed_by: int
    words: int
    custom_translation_statuses: list[TranslationStatus]
    task_id: int
    segment_number: int
