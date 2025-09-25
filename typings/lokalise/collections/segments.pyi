from lokalise.models.segment import SegmentModel
from lokalise.collections.base_collection import BaseCollection

class SegmentsCollection(BaseCollection[SegmentModel]):
    items: list[SegmentModel]
