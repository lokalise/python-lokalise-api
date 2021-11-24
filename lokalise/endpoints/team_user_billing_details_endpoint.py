"""
lokalise.endpoints.team_user_billing_details_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user billing details endpoint.
"""
from .base_endpoint import BaseEndpoint


class TeamUserBillingDetailsEndpoint(BaseEndpoint):
    """Describes team user billing details endpoint.
    """
    PATH = "teams/$parent_id/billing_details"
