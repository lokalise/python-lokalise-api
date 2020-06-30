"""
lokalise.collections.snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing snapshots collection.
"""

from .base_collection import BaseCollection
from ..models.snapshot import SnapshotModel


class SnapshotsCollection(BaseCollection):
    """Describes snapshots.
    """
    DATA_KEY = "snapshots"
    MODEL_KLASS = SnapshotModel
