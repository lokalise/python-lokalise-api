"""
lokalise.client_methods.translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for translations.
"""

from typing import Any

from lokalise.collections.translations import TranslationsCollection
from lokalise.models.translation import TranslationModel

from .endpoint_provider import EndpointProviderMixin


class TranslationMethods(EndpointProviderMixin):
    """Translation client methods."""

    def translations(
        self, project_id: str, params: dict[str, str | int] | None = None
    ) -> TranslationsCollection:
        """Fetches all translations for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request parameters
        :return: Collection of translations
        """
        raw_translations = self.get_endpoint("translations").all(
            params=params, parent_id=project_id
        )
        return TranslationsCollection(raw_translations)

    def translation(
        self,
        project_id: str,
        translation_id: str | int,
        params: dict[str, Any] | None = None,
    ) -> TranslationModel:
        """Fetches a translation.

        :param str project_id: ID of the project
        :param translation_id: ID of the translation to fetch
        :type translation_id: int or str
        :param dict params: (optional) Request parameters
        :return: Task model
        """
        raw_translation = self.get_endpoint("translations").find(
            params, parent_id=project_id, resource_id=translation_id
        )
        return TranslationModel(raw_translation)

    def update_translation(
        self, project_id: str, translation_id: str | int, params: dict[str, Any]
    ) -> TranslationModel:
        """Updates a translation.

        :param str project_id: ID of the project
        :param translation_id: ID of the translation to update
        :type translation_id: int or str
        :param dict params: Translation parameters
        :return: Task model
        """
        raw_translation = self.get_endpoint("translations").update(
            params=params, parent_id=project_id, resource_id=translation_id
        )
        return TranslationModel(raw_translation)
