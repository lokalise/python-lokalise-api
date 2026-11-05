"""
lokalise.endpoints.webhooks_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhooks endpoint.
"""

from .. import request
from .base_endpoint import BaseEndpoint
from ..response import ApiResponse


class WebhooksEndpoint(BaseEndpoint):
    """Describes webhooks endpoint."""

    PATH = "projects/$parent_id/webhooks/$resource_id"

    def regenerate_secret(self, **ids: str | int | None) -> ApiResponse:
        """Regenerates webhook secret.

        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.patch(self.client, path + "/secret/regenerate")
        )
