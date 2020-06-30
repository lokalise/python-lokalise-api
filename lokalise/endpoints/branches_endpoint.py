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
    PATH = "projects/$parent_id/branches/$resource_id"

    def merge(self, params: Optional[Dict[str, Union[str, int]]] = None,
              **ids: Optional[Union[str, int]]) -> Dict:
        """Merges the specified branch into the target branch.

        :param dict params: Merge parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + '/merge', params)
