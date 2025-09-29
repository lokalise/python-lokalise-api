from lokalise.collections.base_collection import BaseCollection
from lokalise.models.branch import BranchModel

class BranchesCollection(BaseCollection[BranchModel]):
    items: list[BranchModel]
