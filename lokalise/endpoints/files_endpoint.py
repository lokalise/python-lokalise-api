"""
lokalise.endpoints.files_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files endpoint.
"""

import warnings
from typing import Any

from .. import request
from .base_endpoint import BaseEndpoint


def _formatwarning(
    msg: str,
    category: type[Warning],
    filename: str,
    lineno: int,
    line: str | None = None,
) -> str:
    return f"{msg}\n"  # pragma: no cover


warnings.formatwarning = _formatwarning


class FilesEndpoint(BaseEndpoint):
    """Describes files endpoint."""

    PATH = "projects/$parent_id/files/$resource_id"

    def upload(self, params: dict[str, Any], **ids: str | int | None) -> dict[str, Any]:
        """Uploads a file to the project.

        :param dict params: Upload parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + "upload", params)

    def download(self, params: dict[str, Any], **ids: str | int | None) -> dict[str, Any]:
        """Downloads files from the project.

        :param dict params: Download parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)

        response = request.post(self.client, path + "download", params)

        if "_response_too_big" in response:
            warnings.warn(
                "Warning: Project is too big for sync export. Please use our async export function "
                "instead (download_files_async)",
                UserWarning,
                stacklevel=2,
            )

        return response

    def download_async(self, params: dict[str, Any], **ids: str | int | None) -> dict[str, Any]:
        """Downloads files from the project asynchronously.

        :param dict params: Download parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + "async-download", params)
