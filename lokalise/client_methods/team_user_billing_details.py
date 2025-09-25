"""
lokalise.client_methods.team_user_billing_details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for team user billing details.
"""

from lokalise.models.team_user_billing_details import TeamUsersBillingDetailsModel

from .endpoint_provider import EndpointProviderMixin


class TeamUserBillingDetailsMethods(EndpointProviderMixin):
    """Team user billing details client methods."""

    def team_user_billing_details(self, team_id: str) -> TeamUsersBillingDetailsModel:
        """Fetches team user billing details.

        :param str team_id: ID of the team
        :return: Team users billing details model
        """
        raw_details = self.get_endpoint("team_user_billing_details").find(parent_id=team_id)
        return TeamUsersBillingDetailsModel(raw_details)

    def create_team_user_billing_details(
        self, team_id: str, params: dict[str, str]
    ) -> TeamUsersBillingDetailsModel:
        """Creates team user billing details.

        :param str team_id: ID of the team
        :param dict params: Billing details parameters
        :return: Team users billing details model
        """
        raw_details = self.get_endpoint("team_user_billing_details").create(
            params=params, parent_id=team_id
        )
        return TeamUsersBillingDetailsModel(raw_details)

    def update_team_user_billing_details(
        self, team_id: str, params: dict[str, str]
    ) -> TeamUsersBillingDetailsModel:
        """Updates team user billing details.

        :param str team_id: ID of the team
        :param dict params: Billing details parameters
        :return: Team users billing details model
        """
        raw_details = self.get_endpoint("team_user_billing_details").update(
            params=params, parent_id=team_id
        )
        return TeamUsersBillingDetailsModel(raw_details)
