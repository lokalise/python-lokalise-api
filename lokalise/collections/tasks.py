"""
lokalise.collections.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing tasks collection.
"""

from ..models.task import TaskModel
from .expert_collection import ExpertCollection


class TasksCollection(ExpertCollection[TaskModel]):
    """Describes tasks."""

    DATA_KEY = "tasks"
    MODEL_KLASS = TaskModel
