"""
lokalise.client_methods.teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for teams.
"""
from typing import Optional, Dict
from lokalise.collections.teams import TeamsCollection
from .endpoint_provider import EndpointProviderMixin


class TeamMethods(EndpointProviderMixin):
    """Team client methods.
    """

    def teams(self, params: Optional[Dict] = None) -> TeamsCollection:
        """Fetches all teams available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of teams
        """
        raw_teams = self.get_endpoint("teams").all(params=params)
        return TeamsCollection(raw_teams)
