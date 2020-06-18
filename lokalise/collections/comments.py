"""
lokalise.collections.comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing comments collection.
"""

from .base_collection import BaseCollection
from ..models.comment import CommentModel


class CommentsCollection(BaseCollection):
    """Describes comments.
    """
    DATA_KEY = "comments"
    MODEL_KLASS = CommentModel
