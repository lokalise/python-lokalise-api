"""
lokalise.models.team_user_group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team user group model.
"""
from .base_model import BaseModel


class TeamUserGroupModel(BaseModel):
    """Describes team user group model.
    """
    DATA_KEY = 'group'

    ATTRS = [
        'group_id',
        'name',
        'permissions',
        'created_at',
        'created_at_timestamp',
        'team_id',
        'projects',
        'members'
    ]
