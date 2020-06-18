"""
lokalise.endpoints.base_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Endpoint parent class inherited by specific endpoints.
"""
from typing import Dict, Optional, Any, Union
import lokalise.client
from .. import request


class BaseEndpoint:
    """Abstract base class for API endpoints. Endpoints are used to load
    the actual data.

    :attribute PATH: contains the relative URI path to the API endpoint, for example
    "/projects" or "/system_languages"
    """
    PATH = ''

    def __init__(self, client: lokalise.client.Client) -> None:
        """Creates a new endpoint.

        :param client: Lokalise API client
        :type client: lokalise.Client
        """
        self.client = client

    def all(self,
            project_id: Optional[str] = None,
            params: Optional[Dict[str, Any]] = None) -> Dict:
        """Loads all items for the given endpoint
        (all projects, all contributors etc).

        :param project_id: ID of the project to load data for
        :param params: Other request parameters like "page" or "limit"
        :rtype dict:
        """
        path = self.PATH.format(
            project_id=project_id if project_id else "",
            resource_id=""
        ).strip('/')
        return request.get(self.client, path, params)

    def find(self, project_id: str,
             resource_id: Optional[Union[str, int]] = None) -> Dict:
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

    def create(self, params: Dict, project_id: Optional[str] = None) -> Dict:
        """Creates a new resource for the given endpoint.

        :param project_id: ID of the project to create resource for
        :param resource_id: resource ID to perform creation for
        :param dict params: Resource parameters
        :rtype dict:
        """

        path = self.PATH.format(
            project_id=project_id if project_id else "",
            resource_id=""
        ).strip('/')
        return request.post(self.client, path, params)

    def update(self, project_id: str, params: Dict,
               resource_id: Optional[Union[str, int]] = None) -> Dict:
        """Updates a resource for the given endpoint.

        :param project_id: ID of the project to update resource for
        :param dict params: Resource parameters
        :rtype dict:
        """

        path = self.PATH.format(
            project_id=project_id if project_id else "",
            resource_id=resource_id if resource_id else ""
        ).strip('/')
        return request.put(self.client, path, params)

    def delete(self, project_id: str,
               resource_id: Optional[Union[str, int]] = None) -> Dict:
        """Deletes a resource for the given endpoint.

        :param project_id: ID of the project to update resource for
        :rtype dict:
        """

        path = self.PATH.format(
            project_id=project_id if project_id else "",
            resource_id=resource_id if resource_id else ""
        ).strip('/')
        return request.delete(self.client, path)
