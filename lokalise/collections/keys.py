"""
lokalise.collections.keys
~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing keys collection.
"""

from ..models.key import KeyModel
from .base_collection import BaseCollection


class KeysCollection(BaseCollection[KeyModel]):
    """Describes keys."""

    DATA_KEY = "keys"
    MODEL_KLASS = KeyModel
