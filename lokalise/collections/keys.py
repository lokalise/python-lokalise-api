"""
lokalise.collections.keys
~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing keys collection.
"""

from .base_collection import BaseCollection
from ..models.key import KeyModel


class KeysCollection(BaseCollection):
    """Describes keys.
    """
    DATA_KEY = "keys"
    MODEL_KLASS = KeyModel
