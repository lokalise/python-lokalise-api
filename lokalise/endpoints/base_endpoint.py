"""
lokalise.endpoints.base_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Endpoint parent class inherited by specific endpoints.
"""

from abc import ABC
from .. import request


class BaseEndpoint(ABC):
    """Abstract base class for API endpoints. Endpoints are used to load
    the actual data.

    :attribute PATH: contains the relative URI path to the API endpoint, for example
    "/projects" or "/system_languages"
    """
    PATH = ''

    def __init__(self, client):
        """Creates a new endpoint.

        :param client: Lokalise API client
        :type client: lokalise.Client
        """
        self.client = client

    def all(self, project_id=None, params={}):
        """Loads all items for the given endpoint
        (all projects, all contributors etc).

        :param project_id: ID of the project to load data for
        :param params: Other request parameters like "page" or "limit"
        :rtype list:
        """
        path = self.PATH.format(
            project_id=project_id if project_id else "",
            resource_id=""
        ).strip('/')
        return request.get(self.client, path, params)

    def find(self, project_id, resource_id=None):
        """Loads an item for the given endpoint
        (one project, one contributor etc).

        :param project_id: ID of the project to load data for
        :param resource_id: resource ID to load
        :rtype dict:
        """
        path = self.PATH.format(
            project_id=project_id,
            resource_id=resource_id if resource_id else ""
        ).strip('/')
        return request.get(self.client, path)
