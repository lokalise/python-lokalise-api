from lokalise.models.team_user import TeamUserModel
from lokalise.collections.base_collection import BaseCollection

class TeamUsersCollection(BaseCollection[TeamUserModel]):
    items: list[TeamUserModel]
