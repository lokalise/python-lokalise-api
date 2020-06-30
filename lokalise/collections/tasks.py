"""
lokalise.collections.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing tasks collection.
"""

from .base_collection import BaseCollection
from ..models.task import TaskModel


class TasksCollection(BaseCollection):
    """Describes tasks.
    """
    DATA_KEY = "tasks"
    MODEL_KLASS = TaskModel
