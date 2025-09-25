"""
lokalise.client_methods.processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for processes.
"""

from typing import Union

from lokalise.collections.queued_processes import QueuedProcessesCollection
from lokalise.models.queued_process import QueuedProcessModel

from .endpoint_provider import EndpointProviderMixin


class ProcessMethods(EndpointProviderMixin):
    """Process client methods."""

    def queued_processes(self, project_id: str) -> QueuedProcessesCollection:
        """Fetches all queued processes for the given project.

        :param str project_id: ID of the project
        :return: Collection of queued processes
        """
        raw_processes = self.get_endpoint("queued_processes").all(parent_id=project_id)
        return QueuedProcessesCollection(raw_processes)

    def queued_process(
        self, project_id: str, queued_process_id: Union[str, int]
    ) -> QueuedProcessModel:
        """Fetches a queued process.

        :param str project_id: ID of the project
        :param queued_process_id: ID of the process to fetch
        :type queued_process_id: int or str
        :return: Queued process model
        """
        raw_process = self.get_endpoint("queued_processes").find(
            parent_id=project_id, resource_id=queued_process_id
        )
        return QueuedProcessModel(raw_process)
