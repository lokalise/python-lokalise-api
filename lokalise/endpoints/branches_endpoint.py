"""
lokalise.endpoints.branches_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches endpoint.
"""

from typing import Any

from .. import request
from .base_endpoint import BaseEndpoint


class BranchesEndpoint(BaseEndpoint):
    """Describes project branches endpoint."""

    PATH = "projects/$parent_id/branches/$resource_id"

    def merge(
        self, params: dict[str, str | int] | None = None, **ids: str | int | None
    ) -> dict[str, Any]:
        """Merges the specified branch into the target branch.

        :param dict params: Merge parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + "/merge", params)
