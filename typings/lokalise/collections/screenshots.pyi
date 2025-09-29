from lokalise.collections.base_collection import BaseCollection
from lokalise.models.screenshot import ScreenshotModel

class ScreenshotsCollection(BaseCollection[ScreenshotModel]):
    items: list[ScreenshotModel]
