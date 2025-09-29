from typing import Any

from lokalise.models.base_model import BaseModel

class ScreenshotModel(BaseModel):
    screenshot_id: int
    key_ids: list[int]
    keys: list[dict[str, Any]]
    url: str
    title: str
    description: str
    screenshot_tags: list[str]
    width: int
    height: int
    created_at: str
    created_at_timestamp: int
