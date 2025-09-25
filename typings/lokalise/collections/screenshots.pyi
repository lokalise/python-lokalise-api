from lokalise.models.screenshot import ScreenshotModel
from lokalise.collections.base_collection import BaseCollection

class ScreenshotsCollection(BaseCollection[ScreenshotModel]):
    items: list[ScreenshotModel]
