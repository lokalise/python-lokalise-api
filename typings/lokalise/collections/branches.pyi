from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.branch import BranchModel

class BranchesCollection(ExpertCollection[BranchModel]):
    items: list[BranchModel]
