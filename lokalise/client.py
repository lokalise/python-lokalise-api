# -*- coding: utf-8 -*-

"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""

from .endpoints.projects import ProjectsEndpoint
from . import request


class Client:
    def __init__(self, token):
        """Instantiate a new Lokalise API client.
        Args:
          token (str):
            Your Lokalise API token.
        """
        self.token = token

    def reset_client(self):
        self.token = None

    def projects(self):
        # projects_endpoint = ProjectsEndpoint(self)
        # projects_endpoint.all()
        request.get(self, "projects")
