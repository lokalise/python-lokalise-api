"""
lokalise.collections.team_users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team users collection.
"""

from .base_collection import BaseCollection
from ..models.team_user import TeamUserModel


class TeamUsersCollection(BaseCollection):
    """Describes team users.
    """
    DATA_KEY = "team_users"
    MODEL_KLASS = TeamUserModel
