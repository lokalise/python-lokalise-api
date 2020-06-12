"""
lokalise.collections.contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing contributors collection.
"""

from .base_collection import BaseCollection
from ..models.contributor import ContributorModel


class ContributorsCollection(BaseCollection):
    """Describes project contributors.
    """
    DATA_KEY = "contributors"
    MODEL_KLASS = ContributorModel
