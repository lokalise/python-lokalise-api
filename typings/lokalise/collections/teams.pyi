from lokalise.models.team import TeamModel
from lokalise.collections.base_collection import BaseCollection

class TeamsCollection(BaseCollection[TeamModel]):
    items: list[TeamModel]
