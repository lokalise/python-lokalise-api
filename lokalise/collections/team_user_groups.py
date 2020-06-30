"""
lokalise.collections.team_user_groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user groups collection.
"""

from .base_collection import BaseCollection
from ..models.team_user_group import TeamUserGroupModel


class TeamUserGroupsCollection(BaseCollection):
    """Describes team user groups.
    """
    DATA_KEY = "user_groups"
    MODEL_KLASS = TeamUserGroupModel
