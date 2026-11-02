"""
lokalise.endpoints.branches_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches endpoint.
"""

from .. import request
from .base_endpoint import BaseEndpoint
from ..response import ApiResponse


class BranchesEndpoint(BaseEndpoint):
    """Describes project branches endpoint."""

    PATH = "projects/$parent_id/branches/$resource_id"

    def merge(
        self, params: dict[str, str | int] | None = None, **ids: str | int | None
    ) -> ApiResponse:
        """Merges the specified branch into the target branch.

        :param dict params: Merge parameters
        :param ids: Identifiers for path generation
        """
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.post(self.client, path + "/merge", params)
        )
