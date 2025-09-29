"""
lokalise.models.team
~~~~~~~~~~~~~~~~~~~~
Module containing team model.
"""

from .base_model import BaseModel


class TeamModel(BaseModel):
    """Describes team model."""

    DATA_KEY = "team"

    ATTRS = [
        "team_id",
        "name",
        "created_at",
        "created_at_timestamp",
        "plan",
        "quota_usage",
        "quota_allowed",
    ]
