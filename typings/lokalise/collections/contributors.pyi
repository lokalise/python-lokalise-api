from lokalise.models.contributor import ContributorModel
from lokalise.collections.base_collection import BaseCollection

class ContributorsCollection(BaseCollection[ContributorModel]):
    items: list[ContributorModel]
