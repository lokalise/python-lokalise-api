from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.contributor import ContributorModel

class ContributorsCollection(ExpertCollection[ContributorModel]):
    items: list[ContributorModel]
