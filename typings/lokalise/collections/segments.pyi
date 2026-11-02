from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.segment import SegmentModel

class SegmentsCollection(ExpertCollection[SegmentModel]):
    items: list[SegmentModel]
