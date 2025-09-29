"""
lokalise.collections.team_user_groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user groups collection.
"""

from ..models.team_user_group import TeamUserGroupModel
from .base_collection import BaseCollection


class TeamUserGroupsCollection(BaseCollection[TeamUserGroupModel]):
    """Describes team user groups."""

    DATA_KEY = "user_groups"
    MODEL_KLASS = TeamUserGroupModel
