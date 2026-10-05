"""
lokalise.client_methods.translation_memories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for translation memories.
"""

from lokalise.collections.translation_memories import TranslationMemoriesCollection

from .endpoint_provider import EndpointProviderMixin


class TranslationMemoriesMethods(EndpointProviderMixin):
    """Screenshot client methods."""

    def translation_memories(self, project_id: str) -> TranslationMemoriesCollection:
        """Fetches all translation memories for the given project.

        :param str project_id: ID of the project
        :return: Collection of translation memories
        """
        raw_tms = self.get_endpoint("translation_memories").all(parent_id=project_id)
        return TranslationMemoriesCollection(raw_tms)
