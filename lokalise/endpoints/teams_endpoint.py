"""
lokalise.endpoints.teams_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing teams endpoint.
"""
from .base_endpoint import BaseEndpoint


class TeamsEndpoint(BaseEndpoint):
    """Describes teams endpoint.
    """
    PATH = "teams"
