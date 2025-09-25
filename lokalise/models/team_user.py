"""
lokalise.models.team_user
~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user model.
"""

from .base_model import BaseModel


class TeamUserModel(BaseModel):
    """Describes team user model."""

    DATA_KEY = "team_user"

    ATTRS = ["user_id", "email", "fullname", "created_at", "created_at_timestamp", "role", "uuid"]
