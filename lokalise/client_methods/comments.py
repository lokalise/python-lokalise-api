"""
lokalise.client_methods.comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for comments.
"""

from typing import Any

from lokalise.collections.comments import CommentsCollection
from lokalise.models.comment import CommentModel

from .endpoint_provider import EndpointProviderMixin


class CommentMethods(EndpointProviderMixin):
    """Comment client methods."""

    def project_comments(
        self, project_id: str, params: dict[str, int | str] | None = None
    ) -> CommentsCollection:
        """Fetches all comments for the given project.

        :param str project_id: ID of the project to fetch comments for.
        :param dict params: (optional) Pagination params
        :return: Collection of comments
        """
        raw_comments = self.get_endpoint("project_comments").all(
            parent_id=project_id, params=params
        )
        return CommentsCollection(raw_comments)

    def key_comments(
        self,
        project_id: str,
        key_id: str | int,
        params: dict[str, int | str] | None = None,
    ) -> CommentsCollection:
        """Fetches all comments for the given key inside a project.

        :param str project_id: ID of the project
        :param key_id: ID of key to fetch comments for
        :type key_id: int or str
        :param dict params: (optional) Pagination params
        :return: Collection of comments
        """
        raw_comments = self.get_endpoint("key_comments").all(
            params=params, parent_id=project_id, resource_id=key_id
        )
        return CommentsCollection(raw_comments)

    def key_comment(
        self, project_id: str, key_id: str | int, comment_id: str | int
    ) -> CommentModel:
        """Fetches a single comment for a given key.

        :param str project_id: ID of the project
        :param key_id: ID of key to fetch comments for
        :type key_id: int or str
        :param comment_id: Comment identifier to fetch
        :type comment_id: int or str
        :return: Comment model
        """
        raw_comment = self.get_endpoint("key_comments").find(
            parent_id=project_id, resource_id=key_id, subresource_id=comment_id
        )
        return CommentModel(raw_comment)

    def create_key_comments(
        self,
        project_id: str,
        key_id: str | int,
        params: list[dict[str, str]] | dict[str, str],
    ) -> CommentsCollection:
        """Creates one or more comments for the given key.

        :param str project_id: ID of the project
        :param key_id: ID of key to create comments for
        :type key_id: int or str
        :param params: Comment parameters
        :type params: list or dict
        :return: Collection of comments
        """
        raw_comments = self.get_endpoint("key_comments").create(
            params=params, wrapper_attr="comments", parent_id=project_id, resource_id=key_id
        )
        return CommentsCollection(raw_comments)

    def delete_key_comment(
        self, project_id: str, key_id: str | int, comment_id: str | int
    ) -> dict[str, Any]:
        """Deletes a given key comment.

        :param str project_id: ID of the project
        :param key_id: ID of key to delete comment for.
        :type key_id: int or str
        :param comment_id: Comment to delete
        :type comment_id: int or str
        :return: Dictionary with project ID and "comment_deleted" set to True
        """
        response = self.get_endpoint("key_comments").delete(
            parent_id=project_id, resource_id=key_id, subresource_id=comment_id
        )
        return response
