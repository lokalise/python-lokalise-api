"""
lokalise.endpoints.files_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files endpoint.
"""

import warnings
from typing import Any

from .. import request
from .base_endpoint import BaseEndpoint
from ..response import ApiResponse


class FilesEndpoint(BaseEndpoint):
    """Describes files endpoint."""

    PATH = "projects/$parent_id/files/$resource_id"

    def upload(self, params: dict[str, Any], **ids: str | int | None) -> ApiResponse:
        """Uploads a file to the project.

        :param dict params: Upload parameters
        :param ids: Identifiers for path generation
        """
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.post(self.client, path + "upload", params)
        )

    def download(self, params: dict[str, Any], **ids: str | int | None) -> ApiResponse:
        """Downloads files from the project.

        :param dict params: Download parameters
        :param ids: Identifiers for path generation
        """
        path = self.path_with_params(**ids)

        response = ApiResponse(
            request.post(self.client, path + "download", params)
        )

        if response.response_too_big:
            warnings.warn(
                "Warning: Project is too big for sync export. "
                "Please use our async export function instead "
                "(download_files_async)",
                UserWarning,
                stacklevel=2,
            )

        return response

    def download_async(self, params: dict[str, Any], **ids: str | int | None) -> ApiResponse:
        """Downloads files from the project asynchronously.

        :param dict params: Download parameters
        :param ids: Identifiers for path generation
        """
        path = self.path_with_params(**ids)
        return ApiResponse(
            request.post(self.client, path + "async-download", params)
        )
