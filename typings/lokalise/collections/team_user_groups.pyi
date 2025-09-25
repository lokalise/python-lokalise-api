from lokalise.models.team_user_group import TeamUserGroupModel
from lokalise.collections.base_collection import BaseCollection

class TeamUserGroupsCollection(BaseCollection[TeamUserGroupModel]):
    items: list[TeamUserGroupModel]
