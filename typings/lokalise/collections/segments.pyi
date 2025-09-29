from lokalise.collections.base_collection import BaseCollection
from lokalise.models.segment import SegmentModel

class SegmentsCollection(BaseCollection[SegmentModel]):
    items: list[SegmentModel]
