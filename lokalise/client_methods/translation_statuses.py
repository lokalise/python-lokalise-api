"""
lokalise.client_methods.translation_statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for translation statuses.
"""

from typing import Any, Optional, Union

from lokalise.collections.translation_statuses import TranslationStatusesCollection
from lokalise.models.translation_status import TranslationStatusModel

from .endpoint_provider import EndpointProviderMixin


class TranslationStatusMethods(EndpointProviderMixin):
    """Translation status client methods."""

    def translation_statuses(
        self, project_id: str, params: Optional[dict[str, str | int]] = None
    ) -> TranslationStatusesCollection:
        """Fetches all translation statuses.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination parameters
        :return: Collection of translation statuses
        """
        raw_statuses = self.get_endpoint("translation_statuses").all(
            params=params, parent_id=project_id
        )
        return TranslationStatusesCollection(raw_statuses)

    def translation_status(
        self,
        project_id: str,
        translation_status_id: Union[str, int],
    ) -> TranslationStatusModel:
        """Fetches a translation status.

        :param str project_id: ID of the project
        :param translation_status_id: ID of the status to fetch
        :type translation_status_id: int or str
        :return: Translation status model
        """
        raw_status = self.get_endpoint("translation_statuses").find(
            parent_id=project_id, resource_id=translation_status_id
        )
        return TranslationStatusModel(raw_status)

    def create_translation_status(
        self, project_id: str, params: dict[str, str]
    ) -> TranslationStatusModel:
        """Creates a translation status.

        :param str project_id: ID of the project
        :param dict params: Translation status parameters
        :return: Translation status model
        """
        raw_status = self.get_endpoint("translation_statuses").create(
            params=params, parent_id=project_id
        )
        return TranslationStatusModel(raw_status)

    def update_translation_status(
        self,
        project_id: str,
        translation_status_id: Union[str, int],
        params: Optional[dict[str, str]] = None,
    ) -> TranslationStatusModel:
        """Updates a translation status.

        :param str project_id: ID of the project
        :param translation_status_id: ID of the status to update
        :type translation_status_id: int or str
        :param dict params: Translation status parameters
        :return: Translation status model
        """
        raw_status = self.get_endpoint("translation_statuses").update(
            params=params, parent_id=project_id, resource_id=translation_status_id
        )
        return TranslationStatusModel(raw_status)

    def delete_translation_status(
        self,
        project_id: str,
        translation_status_id: Union[str, int],
    ) -> dict[str, Any]:
        """Deletes a translation status.

        :param str project_id: ID of the project
        :param translation_status_id: ID of the status to delete
        :type translation_status_id: int or str
        :return: Dict with project ID and `custom_translation_status_deleted`: True
        """
        response = self.get_endpoint("translation_statuses").delete(
            parent_id=project_id, resource_id=translation_status_id
        )
        return response

    def translation_statuses_colors(self, project_id: str) -> list[str]:
        """Fetches available RGB colors that can be assigned to
        translation statuses.

        :param str project_id: ID of the project
        :return: List with the RGB color codes
        """
        response = self.get_endpoint("translation_statuses").colors(parent_id=project_id)
        return response["colors"]
