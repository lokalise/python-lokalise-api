"""
lokalise.collections.keys
~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing keys collection.
"""

from ..models.key import KeyModel
from .expert_collection import ExpertCollection


class KeysCollection(ExpertCollection[KeyModel]):
    """Describes keys."""

    DATA_KEY = "keys"
    MODEL_KLASS = KeyModel
