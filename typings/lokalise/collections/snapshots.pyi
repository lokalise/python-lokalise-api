from lokalise.models.snapshot import SnapshotModel
from lokalise.collections.base_collection import BaseCollection

class SnapshotsCollection(BaseCollection[SnapshotModel]):
    items: list[SnapshotModel]
