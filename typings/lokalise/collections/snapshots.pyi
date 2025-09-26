from lokalise.collections.base_collection import BaseCollection
from lokalise.models.snapshot import SnapshotModel

class SnapshotsCollection(BaseCollection[SnapshotModel]):
    items: list[SnapshotModel]
