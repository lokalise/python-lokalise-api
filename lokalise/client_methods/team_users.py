"""
lokalise.client_methods.team_users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for team users.
"""

from typing import Any, Optional, Union

from lokalise.collections.team_users import TeamUsersCollection
from lokalise.models.team_user import TeamUserModel

from .endpoint_provider import EndpointProviderMixin


class TeamUserMethods(EndpointProviderMixin):
    """Team user client methods."""

    def team_users(
        self, team_id: Union[str, int], params: Optional[dict[str, str | int]] = None
    ) -> TeamUsersCollection:
        """Fetches all team users.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: (optional) Pagination parameters
        :return: Collection of team users
        """
        raw_team_users = self.get_endpoint("team_users").all(params=params, parent_id=team_id)
        return TeamUsersCollection(raw_team_users)

    def team_user(self, team_id: Union[str, int], team_user_id: Union[str, int]) -> TeamUserModel:
        """Fetches a team user.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_id: ID of the team user to fetch
        :type team_user_id: str or int
        :return: Team user model
        """
        raw_team_user = self.get_endpoint("team_users").find(
            parent_id=team_id, resource_id=team_user_id
        )
        return TeamUserModel(raw_team_user)

    def update_team_user(
        self,
        team_id: Union[str, int],
        team_user_id: Union[str, int],
        params: Optional[dict[str, Any]] = None,
    ) -> TeamUserModel:
        """Updates a team user.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_id: ID of the team user to update
        :type team_user_id: str or int
        :param dict params: (optional) Team user parameters
        :return: Team user model
        """
        raw_team_user = self.get_endpoint("team_users").update(
            params=params, parent_id=team_id, resource_id=team_user_id
        )
        return TeamUserModel(raw_team_user)

    def delete_team_user(
        self, team_id: Union[str, int], team_user_id: Union[str, int]
    ) -> dict[str, Any]:
        """Deletes a team user.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_id: ID of the team user to delete
        :type team_user_id: str or int
        :return: Dict with the team ID and `team_user_deleted` set to True
        """
        response = self.get_endpoint("team_users").delete(
            parent_id=team_id, resource_id=team_user_id
        )
        return response
