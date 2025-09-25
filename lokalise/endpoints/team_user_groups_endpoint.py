"""
lokalise.endpoints.team_user_groups_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user groups endpoint.
"""

from typing import Union

from lokalise.utils import to_list

from .. import request
from .base_endpoint import BaseEndpoint


class TeamUserGroupsEndpoint(BaseEndpoint):
    """Describes team user groups endpoint."""

    PATH = "teams/$parent_id/groups/$resource_id"

    def add_projects(self, params: Union[str, list[str]], **ids: Union[str, int]) -> dict:
        """Adds projects represented by IDs to the specified team user group.

        :param params: Projects to add to the group
        :type params: list or str
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.put(self.client, path + "/projects/add", {"projects": to_list(params)})

    def remove_projects(self, params: Union[str, list[str]], **ids: Union[str, int]) -> dict:
        """Removes projects represented by IDs from the specified team user group.

        :param params: Projects to remove from the group
        :type params: list or str
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.put(self.client, path + "/projects/remove", {"projects": to_list(params)})

    def add_members(self, params: Union[str, list[str]], **ids: Union[str, int]) -> dict:
        """Adds members represented by IDs to the specified team user group.

        :param params: Members (users) to add to the group
        :type params: list or str
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.put(self.client, path + "/members/add", {"users": to_list(params)})

    def remove_members(self, params: Union[str, list[str]], **ids: Union[str, int]) -> dict:
        """Removes members represented by IDs from the specified team user group.

        :param params: Members (users) to remove from the group
        :type params: list or str
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.put(self.client, path + "/members/remove", {"users": to_list(params)})
