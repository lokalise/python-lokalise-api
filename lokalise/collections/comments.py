"""
lokalise.collections.comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing comments collection.
"""

from ..models.comment import CommentModel
from .expert_collection import ExpertCollection


class CommentsCollection(ExpertCollection[CommentModel]):
    """Describes comments."""

    DATA_KEY = "comments"
    MODEL_KLASS = CommentModel
