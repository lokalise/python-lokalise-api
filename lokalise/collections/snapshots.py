"""
lokalise.collections.snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing snapshots collection.
"""

from ..models.snapshot import SnapshotModel
from .base_collection import BaseCollection


class SnapshotsCollection(BaseCollection[SnapshotModel]):
    """Describes snapshots."""

    DATA_KEY = "snapshots"
    MODEL_KLASS = SnapshotModel
