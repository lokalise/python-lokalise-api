"""
lokalise.collections.team_user_groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user groups collection.
"""

from ..models.team_user_group import TeamUserGroupModel
from .expert_collection import ExpertCollection


class TeamUserGroupsCollection(ExpertCollection[TeamUserGroupModel]):
    """Describes team user groups."""

    DATA_KEY = "user_groups"
    MODEL_KLASS = TeamUserGroupModel
