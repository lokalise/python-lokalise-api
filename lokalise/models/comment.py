"""
lokalise.models.comment
~~~~~~~~~~~~~~~~~~~~~~~
Module containing comment model.
"""

from .base_model import BaseModel


class CommentModel(BaseModel):
    """Describes comment model.
    """
    DATA_KEY = 'comment'

    ATTRS = [
        'comment_id',
        'key_id',
        'comment',
        'added_by',
        'added_by_email',
        'added_at',
        'added_at_timestamp'
    ]
