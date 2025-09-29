"""
lokalise.collections.comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing comments collection.
"""

from ..models.comment import CommentModel
from .base_collection import BaseCollection


class CommentsCollection(BaseCollection[CommentModel]):
    """Describes comments."""

    DATA_KEY = "comments"
    MODEL_KLASS = CommentModel
