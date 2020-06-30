"""
lokalise.endpoints.base_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Endpoint parent class inherited by specific endpoints.
"""
from typing import Dict, Optional, Any, Union
from string import Template
import lokalise.client
from lokalise.utils import to_list
from .. import request


class BaseEndpoint:
    """Abstract base class for API endpoints. Endpoints are used to load
    the actual data.

    :attribute PATH: contains the template of the relative URI path to
    the API endpoint, for example:

        projects
        projects/system_languages
        projects/$parent_id/contributors
        projects/$parent_id/keys/$resource_id/comments/$subresource_id

    The actual path is generated using the provided ids.
    """
    PATH: str = ''

    def __init__(self, client: lokalise.client.Client) -> None:
        """Creates a new endpoint.

        :param client: Lokalise API client
        :type client: lokalise.Client
        """
        self.client = client

    def all(self, params: Optional[Dict[str, Any]] = None,
            **ids: Optional[Union[str, int]]) -> Dict:
        """Loads all items for the given endpoint
        (all projects, all contributors etc).

        :param dict params: Other request parameters like "page" or "limit"
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.get(self.client, path, params)

    def find(self, params: Optional[Dict[str, Any]] = None,
             **ids: Optional[Union[str, int]]) -> Dict:
        """Loads an item for the given endpoint
        (one project, one contributor etc).

        :param dict params: Other request parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.get(self.client, path, params)

    def create(self, params: Optional[Dict] = None,
               wrapper_attr: Optional[str] = None,
               **ids: Optional[Union[str, int]]) -> Dict:
        """Creates a new resource for the given endpoint.

        :param dict params: Resource parameters
        :param wrapper_attr str: Attribute to wrap the params into. For example:
            [{"comment": "test"}]
        becomes
            {"comments": [{"comment": "test"}]}
        with the `wrapper_attr` set to "comments"
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        if wrapper_attr and params:
            params = {wrapper_attr: to_list(params)}

        path = self.path_with_params(**ids)
        return request.post(self.client, path, params)

    def update(self, params: Dict,
               wrapper_attr: Optional[str] = None,
               **ids: Optional[Union[str, int]]) -> Dict:
        """Updates a resource for the given endpoint.

        :param dict params: Resource parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        if wrapper_attr:
            params = {wrapper_attr: to_list(params)}
        path = self.path_with_params(**ids)
        return request.put(self.client, path, params)

    def delete(self, params: Optional[Dict] = None,
               wrapper_attr: Optional[str] = None,
               **ids: Optional[Union[str, int]]) -> Dict:
        """Deletes a resource for the given endpoint.

        :param ids: Identifiers for path generation
        :rtype dict:
        """
        if wrapper_attr:
            params = {wrapper_attr: params}
        path = self.path_with_params(**ids)
        return request.delete(self.client, path, params)

    def path_with_params(self, **ids: Optional[Union[str, int]]) -> str:
        """Generates relative path to the endpoint using the template stored
        in PATH and the provided ids. Some or all ids may be omitted depending
        on the actual endpoint.
        """
        defaults = dict(parent_id='', resource_id='', subresource_id='')
        return Template(self.PATH).substitute(defaults, **ids)
