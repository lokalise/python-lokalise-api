from lokalise.collections.base_collection import BaseCollection
from lokalise.models.task import TaskModel

class TasksCollection(BaseCollection[TaskModel]):
    items: list[TaskModel]
