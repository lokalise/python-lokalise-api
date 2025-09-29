"""
lokalise.client_methods.languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for languages.
"""

from typing import Any

from lokalise.collections.languages import LanguagesCollection
from lokalise.models.language import LanguageModel

from .endpoint_provider import EndpointProviderMixin


class LanguageMethods(EndpointProviderMixin):
    """Language client methods."""

    def system_languages(self, params: dict[str, str | int] | None = None) -> LanguagesCollection:
        """Fetches all languages that Lokalise supports.

        :param dict params: (optional) Pagination params
        :return: Collection of languages
        """
        raw_languages = self.get_endpoint("system_languages").all(params=params)
        return LanguagesCollection(raw_languages)

    def project_languages(
        self, project_id: str, params: dict[str, str | int] | None = None
    ) -> LanguagesCollection:
        """Fetches all languages for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of languages
        """
        raw_languages = self.get_endpoint("languages").all(parent_id=project_id, params=params)
        return LanguagesCollection(raw_languages)

    def create_languages(
        self, project_id: str, params: list[dict[str, Any]] | dict[str, Any]
    ) -> LanguagesCollection:
        """Create one or more languages for the given project.

        :param str project_id: ID of the project
        :param params: Language parameters
        :type params: dict or list
        :return: Collection of languages
        """
        raw_languages = self.get_endpoint("languages").create(
            params=params, wrapper_attr="languages", parent_id=project_id
        )
        return LanguagesCollection(raw_languages)

    def language(self, project_id: str, language_id: str | int) -> LanguageModel:
        """Fetches a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to fetch
        :return: Language model
        """
        raw_language = self.get_endpoint("languages").find(
            parent_id=project_id, resource_id=language_id
        )
        return LanguageModel(raw_language)

    def update_language(
        self, project_id: str, language_id: str | int, params: dict[str, Any]
    ) -> LanguageModel:
        """Updates a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to update
        :param dict params: Update parameters
        :return: Language model
        """
        raw_language = self.get_endpoint("languages").update(
            params=params, parent_id=project_id, resource_id=language_id
        )
        return LanguageModel(raw_language)

    def delete_language(self, project_id: str, language_id: str | int) -> dict[str, Any]:
        """Deletes a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to delete
        :return: Dictionary with project ID and "language_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("languages").delete(
            parent_id=project_id, resource_id=language_id
        )
        return response
