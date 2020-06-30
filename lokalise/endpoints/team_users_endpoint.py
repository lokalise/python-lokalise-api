"""
lokalise.endpoints.team_users_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team users endpoint.
"""
from .base_endpoint import BaseEndpoint


class TeamUsersEndpoint(BaseEndpoint):
    """Describes team users endpoint.
    """
    PATH = "teams/$parent_id/users/$resource_id"
