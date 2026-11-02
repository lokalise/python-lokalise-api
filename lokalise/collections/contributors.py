"""
lokalise.collections.contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing contributors collection.
"""

from ..models.contributor import ContributorModel
from .expert_collection import ExpertCollection


class ContributorsCollection(ExpertCollection[ContributorModel]):
    """Describes project contributors."""

    DATA_KEY = "contributors"
    MODEL_KLASS = ContributorModel
