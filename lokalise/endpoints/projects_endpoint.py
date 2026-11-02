"""
lokalise.endpoints.projects_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects endpoint.
"""

from typing import Any

from .. import request
from .base_endpoint import BaseEndpoint
from ..response import ApiResponse


class ProjectsEndpoint(BaseEndpoint):
    """Describes projects endpoint."""

    PATH = "projects/$parent_id"

    def empty(self, **ids: str | int | None) -> dict[str, Any]:
        """Empties a given project by removing all keys and translations.

        :param ids: IDs to generate the proper path
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.put(self.client, path + "/empty")
        )
