from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.screenshot import ScreenshotModel

class ScreenshotsCollection(ExpertCollection[ScreenshotModel]):
    items: list[ScreenshotModel]
