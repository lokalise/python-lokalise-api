"""
lokalise.models.contributor
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing contributor model.
"""

from .base_model import BaseModel


class ContributorModel(BaseModel):
    """Describes project contributors model."""

    DATA_KEY = "contributor"

    ATTRS = [
        "user_id",
        "email",
        "fullname",
        "created_at",
        "created_at_timestamp",
        "is_admin",
        "is_reviewer",
        "languages",
        "admin_rights",
        "role_id",
        "uuid",
    ]
