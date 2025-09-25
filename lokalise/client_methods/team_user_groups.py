"""
lokalise.client_methods.team_user_groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for team user groups.
"""

from typing import Any, Optional, Union

from lokalise.collections.team_user_groups import TeamUserGroupsCollection
from lokalise.models.team_user_group import TeamUserGroupModel

from .endpoint_provider import EndpointProviderMixin


class TeamUserGroupMethods(EndpointProviderMixin):
    """Team user group client methods."""

    def team_user_groups(
        self, team_id: Union[str, int], params: Optional[dict[str, str | int]] = None
    ) -> TeamUserGroupsCollection:
        """Fetches all team user groups.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: (optional) Pagination parameters
        :return: Collection of team user groups
        """
        raw_groups = self.get_endpoint("team_user_groups").all(params=params, parent_id=team_id)
        return TeamUserGroupsCollection(raw_groups)

    def team_user_group(
        self, team_id: Union[str, int], team_user_group_id: Union[str, int]
    ) -> TeamUserGroupModel:
        """Fetches a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to fetch
        :type team_user_group_id: str or int
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").find(
            parent_id=team_id, resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def create_team_user_group(
        self, team_id: Union[str, int], params: dict[str, Any]
    ) -> TeamUserGroupModel:
        """Fetches a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: Team user group parameters
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").create(params=params, parent_id=team_id)
        return TeamUserGroupModel(raw_group)

    def update_team_user_group(
        self, team_id: Union[str, int], team_user_group_id: Union[str, int], params: dict[str, Any]
    ) -> TeamUserGroupModel:
        """Updates a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to update
        :type team_user_group_id: str or int
        :param dict params: Team user group parameters
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").update(
            params=params, parent_id=team_id, resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def delete_team_user_group(
        self, team_id: Union[str, int], team_user_group_id: Union[str, int]
    ) -> dict[str, Any]:
        """Deletes a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to delete
        :type team_user_group_id: str or int
        :return: Dict with team ID and `group_deleted` set to True
        """
        response = self.get_endpoint("team_user_groups").delete(
            parent_id=team_id, resource_id=team_user_group_id
        )
        return response

    def add_projects_to_group(
        self,
        team_id: Union[str, int],
        team_user_group_id: Union[str, int],
        params: Union[str, list[str]],
    ) -> TeamUserGroupModel:
        """Adds projects to a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to add projects to
        :type team_user_group_id: str or int
        :param params: Project IDs to add to the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").add_projects(
            params=params, parent_id=team_id, resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def remove_projects_from_group(
        self,
        team_id: Union[str, int],
        team_user_group_id: Union[str, int],
        params: Union[str, list[str]],
    ) -> TeamUserGroupModel:
        """Removes projects from a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to remove projects from
        :type team_user_group_id: str or int
        :param params: Project IDs to remove from the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").remove_projects(
            params=params, parent_id=team_id, resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def add_members_to_group(
        self,
        team_id: Union[str, int],
        team_user_group_id: Union[str, int],
        params: Union[str, list[str]],
    ) -> TeamUserGroupModel:
        """Adds members to a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to add members to
        :type team_user_group_id: str or int
        :param params: User IDs to add to the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").add_members(
            params=params, parent_id=team_id, resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def remove_members_from_group(
        self,
        team_id: Union[str, int],
        team_user_group_id: Union[str, int],
        params: Union[str, list[str]],
    ) -> TeamUserGroupModel:
        """Removes members from a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to remove members from
        :type team_user_group_id: str or int
        :param params: User IDs to remove from the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").remove_members(
            params=params, parent_id=team_id, resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)
