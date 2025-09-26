from lokalise.collections.base_collection import BaseCollection
from lokalise.models.team_user_group import TeamUserGroupModel

class TeamUserGroupsCollection(BaseCollection[TeamUserGroupModel]):
    items: list[TeamUserGroupModel]
