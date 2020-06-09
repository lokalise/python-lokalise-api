from .base_collection import BaseCollection
from ..models.contributor import ContributorModel


class ContributorsCollection(BaseCollection):
    DATA_KEY = "contributors"
    MODEL_KLASS = ContributorModel
