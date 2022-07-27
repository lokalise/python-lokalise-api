"""
lokalise.endpoints.files_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files endpoint.
"""
from typing import Dict, Union, Any, Optional
from .base_endpoint import BaseEndpoint
from .. import request


class FilesEndpoint(BaseEndpoint):
    """Describes files endpoint.
    """
    PATH = "projects/$parent_id/files/$resource_id"

    def upload(self, params: Dict[str, Any],
               **ids: Optional[Union[str, int]]) -> Dict:
        """Uploads a file to the project.

        :param dict params: Upload parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + 'upload', params)

    def download(self, params: Dict[str, Any],
                 **ids: Optional[Union[str, int]]) -> Dict:
        """Downloads files from the project.

        :param dict params: Download parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + 'download', params)
