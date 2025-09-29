from lokalise.collections.base_collection import BaseCollection
from lokalise.models.team import TeamModel

class TeamsCollection(BaseCollection[TeamModel]):
    items: list[TeamModel]
