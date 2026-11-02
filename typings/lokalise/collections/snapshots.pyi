from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.snapshot import SnapshotModel

class SnapshotsCollection(ExpertCollection[SnapshotModel]):
    items: list[SnapshotModel]
