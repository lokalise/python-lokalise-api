from lokalise.collections.base_collection import BaseCollection
from lokalise.models.team_user import TeamUserModel

class TeamUsersCollection(BaseCollection[TeamUserModel]):
    items: list[TeamUserModel]
