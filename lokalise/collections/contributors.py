"""
lokalise.collections.contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing contributors collection.
"""

from ..models.contributor import ContributorModel
from .base_collection import BaseCollection


class ContributorsCollection(BaseCollection[ContributorModel]):
    """Describes project contributors."""

    DATA_KEY = "contributors"
    MODEL_KLASS = ContributorModel
