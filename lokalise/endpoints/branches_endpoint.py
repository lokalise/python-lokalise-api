"""
lokalise.endpoints.branches_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches endpoint.
"""
from typing import Dict, Union, Optional
from .base_endpoint import BaseEndpoint
from .. import request


class BranchesEndpoint(BaseEndpoint):
    """Describes project branches endpoint.
    """
    PATH = "projects/{project_id}/branches/{resource_id}"

    def merge(self, project_id: str, branch_id: Union[str, int],
              params: Optional[Dict[str, Union[str, int]]] = None) -> Dict:
        """Merges the specified branch into the target branch.

        :param project_id: ID of the project
        :param branch_id: ID of the source branch
        :type branch_id: int or str
        :param dict params: Merge parameters
        :rtype dict:
        """
        path = self.PATH.format(
            project_id=project_id,
            resource_id=branch_id
        ) + '/merge'
        return request.post(self.client, path, params)
