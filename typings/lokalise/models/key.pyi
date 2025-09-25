from typing import Literal, TypedDict

from typing_extensions import NotRequired

from lokalise.models.base_model import BaseModel

class TranslationStatusDict(TypedDict):
    status_id: int
    title: str
    color: str

class TranslationDict(TypedDict):
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
    custom_translation_statuses: list[TranslationStatusDict]
    task_id: int
    segment_number: int

class ScreenshotKeyCoordinates(TypedDict):
    left: int
    top: int
    width: int
    height: int

class ScreenshotKey(TypedDict):
    key_id: int
    coordinates: ScreenshotKeyCoordinates

class ScreenshotDict(TypedDict):
    screenshot_id: int
    key_ids: list[int]
    keys: list[ScreenshotKey]
    url: str
    title: str
    description: str
    screenshot_tags: list[str]
    width: int
    height: int
    created_at: str
    created_at_timestamp: int

class CommentDict(TypedDict):
    comment_id: int
    key_id: int
    comment: str
    added_by: int
    added_by_email: str
    added_at: str
    added_at_timestamp: int

class KeyCommentDict(TypedDict):
    comment_id: int
    comment: str
    added_by: int
    added_by_email: str
    added_at: str
    added_at_timestamp: int

class Filenames(TypedDict, total=False):
    ios: NotRequired[str | None]
    android: NotRequired[str | None]
    web: NotRequired[str | None]
    other: NotRequired[str | None]

Keynames = Filenames

SupportedPlatforms = Literal["ios", "android", "web", "other"]

class KeyModel(BaseModel):
    key_id: int
    created_at: str
    created_at_timestamp: int
    key_name: Keynames
    filenames: Filenames
    description: str
    platforms: list[SupportedPlatforms]
    tags: list[str]
    comments: list[KeyCommentDict]
    screenshots: list[ScreenshotDict]
    translations: list[TranslationDict]
    is_plural: bool
    plural_name: str
    is_hidden: bool
    is_archived: bool
    context: str
    base_words: int
    char_limit: int
    custom_attributes: str
    modified_at: str
    modified_at_timestamp: int
    translations_modified_at: str
    translations_modified_at_timestamp: int
