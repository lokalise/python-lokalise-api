"""
lokalise.endpoints.projects_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects endpoint.
"""

from typing import Optional, Union

from .. import request
from .base_endpoint import BaseEndpoint


class ProjectsEndpoint(BaseEndpoint):
    """Describes projects endpoint."""

    PATH = "projects/$parent_id"

    def empty(self, **ids: Optional[Union[str, int]]) -> dict:
        """Empties a given project by removing all keys and translations.

        :param ids: IDs to generate the proper path
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.put(self.client, path + "/empty")
