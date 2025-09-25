from lokalise.models.task import TaskModel
from lokalise.collections.base_collection import BaseCollection

class TasksCollection(BaseCollection[TaskModel]):
    items: list[TaskModel]
