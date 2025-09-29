"""
lokalise.collections.branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches collection.
"""

from ..models.branch import BranchModel
from .base_collection import BaseCollection


class BranchesCollection(BaseCollection[BranchModel]):
    """Describes project branches."""

    DATA_KEY = "branches"
    MODEL_KLASS = BranchModel
