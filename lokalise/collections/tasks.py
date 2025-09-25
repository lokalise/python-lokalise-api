"""
lokalise.collections.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing tasks collection.
"""

from ..models.task import TaskModel
from .base_collection import BaseCollection


class TasksCollection(BaseCollection[TaskModel]):
    """Describes tasks."""

    DATA_KEY = "tasks"
    MODEL_KLASS = TaskModel
