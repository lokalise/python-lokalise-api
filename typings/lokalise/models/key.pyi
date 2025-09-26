from typing import Any, Literal

from lokalise.models.base_model import BaseModel

SupportedPlatforms = Literal["ios", "android", "web", "other"]

class KeyModel(BaseModel):
    key_id: int
    created_at: str
    created_at_timestamp: int
    key_name: dict[str, Any]
    filenames: dict[str, Any]
    description: str
    platforms: list[SupportedPlatforms]
    tags: list[str]
    comments: list[dict[str, Any]]
    screenshots: list[dict[str, Any]]
    translations: list[dict[str, Any]]
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
