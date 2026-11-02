"""
lokalise.collections.branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches collection.
"""

from ..models.branch import BranchModel
from .expert_collection import ExpertCollection


class BranchesCollection(ExpertCollection[BranchModel]):
    """Describes project branches."""

    DATA_KEY = "branches"
    MODEL_KLASS = BranchModel
