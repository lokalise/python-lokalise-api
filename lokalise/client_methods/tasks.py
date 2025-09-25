"""
lokalise.client_methods.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for tasks.
"""

from typing import Any, Optional, Union

from lokalise.collections.tasks import TasksCollection
from lokalise.models.task import TaskModel

from .endpoint_provider import EndpointProviderMixin


class TaskMethods(EndpointProviderMixin):
    """Task client methods."""

    def tasks(
        self, project_id: str, params: Optional[dict[str, str | int]] = None
    ) -> TasksCollection:
        """Fetches all tasks for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request parameters
        :return: Collection of tasks
        """
        raw_tasks = self.get_endpoint("tasks").all(params=params, parent_id=project_id)
        return TasksCollection(raw_tasks)

    def task(self, project_id: str, task_id: Union[str, int]) -> TaskModel:
        """Fetches a task.

        :param str project_id: ID of the project
        :param task_id: ID of the task to fetch
        :type task_id: int or str
        :return: Task model
        """
        raw_task = self.get_endpoint("tasks").find(parent_id=project_id, resource_id=task_id)
        return TaskModel(raw_task)

    def create_task(self, project_id: str, params: dict[str, Any]) -> TaskModel:
        """Creates a task in the given project.

        :param str project_id: ID of the project
        :param dict params: Task parameters
        :return: Task model
        """
        raw_task = self.get_endpoint("tasks").create(params=params, parent_id=project_id)
        return TaskModel(raw_task)

    def update_task(
        self, project_id: str, task_id: Union[str, int], params: Optional[dict[str, Any]] = None
    ) -> TaskModel:
        """Updates a task.

        :param str project_id: ID of the project
        :param task_id: ID of the task to update
        :type task_id: int or str
        :param dict params: Task parameters
        :return: Task model
        """
        raw_task = self.get_endpoint("tasks").update(
            params=params, parent_id=project_id, resource_id=task_id
        )
        return TaskModel(raw_task)

    def delete_task(self, project_id: str, task_id: Union[str, int]) -> dict[str, Any]:
        """Deletes a task.

        :param str project_id: ID of the project
        :param task_id: ID of the task to delete
        :type task_id: int or str
        :return: Dictionary with the project ID and "task_deleted": True
        """
        response = self.get_endpoint("tasks").delete(parent_id=project_id, resource_id=task_id)
        return response
