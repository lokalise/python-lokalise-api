from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.team_user_group import TeamUserGroupModel

class TeamUserGroupsCollection(ExpertCollection[TeamUserGroupModel]):
    items: list[TeamUserGroupModel]
