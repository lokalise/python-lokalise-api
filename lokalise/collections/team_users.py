"""
lokalise.collections.team_users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team users collection.
"""

from ..models.team_user import TeamUserModel
from .expert_collection import ExpertCollection


class TeamUsersCollection(ExpertCollection[TeamUserModel]):
    """Describes team users."""

    DATA_KEY = "team_users"
    MODEL_KLASS = TeamUserModel
