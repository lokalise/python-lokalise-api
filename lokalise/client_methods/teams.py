"""
lokalise.client_methods.teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for teams.
"""

from typing import Optional, Union

from lokalise.collections.teams import TeamsCollection
from lokalise.models.team import TeamModel

from .endpoint_provider import EndpointProviderMixin


class TeamMethods(EndpointProviderMixin):
    """Team client methods."""

    def teams(self, params: Optional[dict[str, str | int]] = None) -> TeamsCollection:
        """Fetches all teams available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of teams
        """
        raw_teams = self.get_endpoint("teams").all(params=params)
        return TeamsCollection(raw_teams)

    def team(self, team_id: Union[str, int]) -> TeamModel:
        """Fetches a single team by ID.

        :param team_id: ID of the team to fetch
        :type team_id: int or str
        :return: Team model
        """
        raw_project = self.get_endpoint("teams").find(parent_id=team_id)
        return TeamModel(raw_project)
