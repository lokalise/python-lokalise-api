"""
lokalise.endpoints.base_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Endpoint parent class inherited by specific endpoints.
"""

from string import Template
from typing import TYPE_CHECKING, Any

from ..utils import to_list

if TYPE_CHECKING:
    from ..base_client import BaseClient

from .. import request
from ..response import ApiResponse


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

    PATH: str = ""

    def __init__(self, client: "BaseClient") -> None:
        """Creates a new endpoint.

        :param client: Lokalise API client
        :type client: lokalise.client.Client
        """
        self.client = client

    def all(
        self,
        params: dict[str, Any] | None = None,
        **ids: str | int | None,
    ) -> ApiResponse:
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.get(self.client, path, params)
        )

    def find(
        self,
        params: dict[str, Any] | None = None,
        **ids: str | int | None,
    ) -> ApiResponse:
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.get(self.client, path, params)
        )

    def create(
        self,
        params: dict[str, Any] | None = None,
        wrapper_attr: str | None = None,
        **ids: str | int | None,
    ) -> ApiResponse:
        if wrapper_attr and params is not None:
            params = {wrapper_attr: to_list(params)}

        path = self.path_with_params(**ids)
        return ApiResponse(
            request.post(self.client, path, params)
        )

    def update(
        self,
        params: dict[str, Any],
        wrapper_attr: str | None = None,
        **ids: str | int | None,
    ) -> ApiResponse:
        if wrapper_attr:
            params = {wrapper_attr: to_list(params)}
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.put(self.client, path, params)
        )

    def delete(
        self,
        params: dict[str, Any] | None = None,
        wrapper_attr: str | None = None,
        **ids: str | int | None,
    ) -> ApiResponse:
        if wrapper_attr:
            params = {wrapper_attr: params}
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.delete(self.client, path, params)
        )

    def path_with_params(self, **ids: str | int | None) -> str:
        """Generate a relative endpoint path using PATH and the provided IDs."""
        values: dict[str, str | int] = {
            "parent_id": "",
            "resource_id": "",
            "subresource_id": "",
        }
        values.update({key: value for key, value in ids.items() if value is not None})

        try:
            return Template(self.PATH).substitute(values)
        except KeyError as exc:
            raise ValueError(f"Missing required path parameter: {exc}") from None
