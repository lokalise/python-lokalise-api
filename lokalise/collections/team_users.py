"""
lokalise.collections.team_users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team users collection.
"""

from ..models.team_user import TeamUserModel
from .base_collection import BaseCollection


class TeamUsersCollection(BaseCollection[TeamUserModel]):
    """Describes team users."""

    DATA_KEY = "team_users"
    MODEL_KLASS = TeamUserModel
