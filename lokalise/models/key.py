"""
lokalise.models.key
~~~~~~~~~~~~~~~~~~~
Module containing key model.
"""

from .base_model import BaseModel


class KeyModel(BaseModel):
    """Describes key model."""

    DATA_KEY = "key"

    ATTRS = [
        "key_id",
        "created_at",
        "created_at_timestamp",
        "key_name",
        "filenames",
        "description",
        "platforms",
        "tags",
        "comments",
        "screenshots",
        "translations",
        "is_plural",
        "plural_name",
        "is_hidden",
        "is_archived",
        "context",
        "base_words",
        "char_limit",
        "custom_attributes",
        "modified_at",
        "modified_at_timestamp",
        "translations_modified_at",
        "translations_modified_at_timestamp",
    ]
