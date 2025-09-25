"""
lokalise.client_methods.files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for files.
"""

from typing import Any, Optional, Union

from lokalise.collections.files import FilesCollection
from lokalise.models.queued_process import QueuedProcessModel

from .endpoint_provider import EndpointProviderMixin


class FileMethods(EndpointProviderMixin):
    """File client methods."""

    def files(
        self, project_id: str, params: Optional[dict[str, Union[int, str]]] = None
    ) -> FilesCollection:
        """Fetches all files for the given project.

        :param str project_id: ID of the project to fetch files for.
        :param dict params: (optional) Pagination params
        :return: Collection of files
        """
        raw_files = self.get_endpoint("files").all(parent_id=project_id, params=params)
        return FilesCollection(raw_files)

    def upload_file(self, project_id: str, params: dict[str, Any]) -> QueuedProcessModel:
        """Uploads a file to the given project.

        :param str project_id: ID of the project to upload file to
        :param dict params: Upload params
        :return: Queued process model
        """
        raw_process = self.get_endpoint("files").upload(params=params, parent_id=project_id)
        return QueuedProcessModel(raw_process)

    def download_files(self, project_id: str, params: dict[str, Any]) -> dict[str, str]:
        """Downloads files from the given project.

        :param str project_id: ID of the project to download from
        :param dict params: Download params
        :return: Dictionary with project ID and a bundle URL
        """
        response = self.get_endpoint("files").download(params=params, parent_id=project_id)
        return response

    def download_files_async(self, project_id: str, params: dict[str, Any]) -> QueuedProcessModel:
        """Downloads files from the given project asynchronously.

        :param str project_id: ID of the project to download file from
        :param dict params: Download params
        :return: Queued process model
        """
        raw_process = self.get_endpoint("files").download_async(params=params, parent_id=project_id)
        return QueuedProcessModel(raw_process)

    def delete_file(self, project_id: str, file_id: Union[str, int]) -> dict[str, Any]:
        """Deletes a file and it's associated keys from the project.
        File __unassigned__ cannot be deleted.
        This endpoint does not support "software localization" projects.

        :param str project_id: ID of the project
        :param file_id: ID of the file to delete
        :return: Dictionary with project ID and "file_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("files").delete(parent_id=project_id, resource_id=file_id)
        return response
