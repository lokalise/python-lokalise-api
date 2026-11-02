"""
lokalise.collections.queued_processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued processes collection.
"""

from ..models.queued_process import QueuedProcessModel
from .expert_collection import ExpertCollection


class QueuedProcessesCollection(ExpertCollection[QueuedProcessModel]):
    """Describes queued processes."""

    DATA_KEY = "processes"
    MODEL_KLASS = QueuedProcessModel
