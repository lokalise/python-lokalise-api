from lokalise.collections.base_collection import BaseCollection
from lokalise.models.contributor import ContributorModel

class ContributorsCollection(BaseCollection[ContributorModel]):
    items: list[ContributorModel]
