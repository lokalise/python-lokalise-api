"""
lokalise.client_methods.keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for keys.
"""

from typing import Any

from lokalise.collections.keys import KeysCollection
from lokalise.models.key import KeyModel

from .endpoint_provider import EndpointProviderMixin


class KeyMethods(EndpointProviderMixin):
    """Key client methods."""

    def keys(self, project_id: str, params: dict[str, Any] | None = None) -> KeysCollection:
        """Fetches all keys for the given project.

        :param str project_id: ID of the project
        :param dict params: Request parameters
        :return: Collection of keys
        """
        raw_keys = self.get_endpoint("keys").all(parent_id=project_id, params=params)
        return KeysCollection(raw_keys)

    def create_keys(
        self, project_id: str, params: dict[str, Any] | list[dict[str, Any]]
    ) -> KeysCollection:
        """Creates one or more keys inside the project

        :param str project_id: ID of the project
        :param params: Keys parameters
        :type params: list or dict
        :return: Keys collection
        """
        raw_keys = self.get_endpoint("keys").create(
            params=params, wrapper_attr="keys", parent_id=project_id
        )

        return KeysCollection(raw_keys)

    def key(
        self, project_id: str, key_id: str | int, params: dict[str, Any] | None = None
    ) -> KeyModel:
        """Fetches a translation key.

        :param str project_id: ID of the project
        :param key_id: ID of the key to fetch
        :param dict params: Request parameters
        :return: Key model
        """
        raw_key = self.get_endpoint("keys").find(
            params=params, parent_id=project_id, resource_id=key_id
        )
        return KeyModel(raw_key)

    def update_key(
        self, project_id: str, key_id: str | int, params: dict[str, Any] | None = None
    ) -> KeyModel:
        """Updates a translation key.

        :param str project_id: ID of the project
        :param key_id: ID of the key to update
        :param dict params: Request parameters
        :return: Key model
        """
        raw_key = self.get_endpoint("keys").update(
            params=params, parent_id=project_id, resource_id=key_id
        )
        return KeyModel(raw_key)

    def update_keys(
        self, project_id: str, params: list[dict[str, Any]] | dict[str, Any]
    ) -> KeysCollection:
        """Updates translation keys in bulk.

        :param str project_id: ID of the project
        :param dict params: Key parameters
        :return: Key collection
        """
        raw_keys = self.get_endpoint("keys").update(
            params=params, wrapper_attr="keys", parent_id=project_id
        )
        return KeysCollection(raw_keys)

    def delete_key(self, project_id: str, key_id: str | int) -> dict[str, Any]:
        """Deletes a key.

        :param str project_id: ID of the project
        :param key_id: ID of the key to delete
        :type key_id: int or str
        :return: Dictionary with project ID and "key_removed" set to True
        :rtype dict:
        """
        response = self.get_endpoint("keys").delete(parent_id=project_id, resource_id=key_id)
        return response

    def delete_keys(self, project_id: str, key_ids: list[str | int]) -> dict[str, Any]:
        """Deletes keys in bulk.

        :param str project_id: ID of the project
        :type key_id: int or str
        :param list key_ids: List of the key identifiers to delete
        :return: Dictionary with project ID and "keys_removed" set to True
        :rtype dict:
        """
        response = self.get_endpoint("keys").delete(
            params=key_ids, wrapper_attr="keys", parent_id=project_id
        )
        return response
