"""
lokalise.collections.queued_processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued processes collection.
"""

from .base_collection import BaseCollection
from ..models.queued_process import QueuedProcessModel


class QueuedProcessesCollection(BaseCollection):
    """Describes queued processes.
    """
    DATA_KEY = "processes"
    MODEL_KLASS = QueuedProcessModel
