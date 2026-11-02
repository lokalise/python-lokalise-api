from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.task import TaskModel

class TasksCollection(ExpertCollection[TaskModel]):
    items: list[TaskModel]
