"""
lokalise.collections.branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches collection.
"""

from .base_collection import BaseCollection
from ..models.branch import BranchModel


class BranchesCollection(BaseCollection):
    """Describes project branches.
    """
    DATA_KEY = "branches"
    MODEL_KLASS = BranchModel
