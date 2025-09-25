"""
lokalise.models.snapshot
~~~~~~~~~~~~~~~~~~~~~~~~
Module containing snapshot model.
"""

from .base_model import BaseModel


class SnapshotModel(BaseModel):
    """Describes project snapshot."""

    DATA_KEY = "snapshot"

    ATTRS = [
        "snapshot_id",
        "title",
        "created_at",
        "created_at_timestamp",
        "created_by",
        "created_by_email",
    ]
