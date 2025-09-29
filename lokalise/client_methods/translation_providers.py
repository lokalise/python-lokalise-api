"""
lokalise.client_methods.translation_providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for translation providers.
"""

from lokalise.collections.translation_providers import TranslationProvidersCollection
from lokalise.models.translation_provider import TranslationProviderModel

from .endpoint_provider import EndpointProviderMixin


class TranslationProviderMethods(EndpointProviderMixin):
    """Translation provider client methods."""

    def translation_providers(
        self, team_id: str | int, params: dict[str, str | int] | None = None
    ) -> TranslationProvidersCollection:
        """Fetches all translation providers.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: (optional) Pagination parameters
        :return: Collection of translation providers
        """
        raw_providers = self.get_endpoint("translation_providers").all(
            params=params, parent_id=team_id
        )
        return TranslationProvidersCollection(raw_providers)

    def translation_provider(
        self, team_id: str | int, translation_provider_id: str | int
    ) -> TranslationProviderModel:
        """Fetches a translation provider.

        :param team_id: ID of the team
        :type team_id: str or int
        :param translation_provider_id: ID of the translation provider to fetch
        :type translation_provider_id: str or int
        :return: Translation provider model
        """
        raw_provider = self.get_endpoint("translation_providers").find(
            parent_id=team_id, resource_id=translation_provider_id
        )
        return TranslationProviderModel(raw_provider)
