from lokalise.models.branch import BranchModel
from lokalise.collections.base_collection import BaseCollection

class BranchesCollection(BaseCollection[BranchModel]):
    items: list[BranchModel]
