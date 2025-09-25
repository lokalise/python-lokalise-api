from typing import TypedDict

from lokalise.models.base_model import BaseModel

class ScreenshotKeyCoordinates(TypedDict):
    left: int
    top: int
    width: int
    height: int

class ScreenshotKey(TypedDict):
    key_id: int
    coordinates: ScreenshotKeyCoordinates

class ScreenshotModel(BaseModel):
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
