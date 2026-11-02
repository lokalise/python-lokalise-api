from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.team_user import TeamUserModel

class TeamUsersCollection(ExpertCollection[TeamUserModel]):
    items: list[TeamUserModel]
