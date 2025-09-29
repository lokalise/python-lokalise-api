"""
lokalise.collections.queued_processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued processes collection.
"""

from ..models.queued_process import QueuedProcessModel
from .base_collection import BaseCollection


class QueuedProcessesCollection(BaseCollection[QueuedProcessModel]):
    """Describes queued processes."""

    DATA_KEY = "processes"
    MODEL_KLASS = QueuedProcessModel
