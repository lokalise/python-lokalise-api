"""
lokalise.collections.snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing snapshots collection.
"""

from ..models.snapshot import SnapshotModel
from .expert_collection import ExpertCollection


class SnapshotsCollection(ExpertCollection[SnapshotModel]):
    """Describes snapshots."""

    DATA_KEY = "snapshots"
    MODEL_KLASS = SnapshotModel
