from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.team import TeamModel

class TeamsCollection(ExpertCollection[TeamModel]):
    items: list[TeamModel]
