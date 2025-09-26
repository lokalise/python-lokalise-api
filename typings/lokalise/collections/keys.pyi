from typing import Any

from lokalise.collections.base_collection import BaseCollection
from lokalise.models.key import KeyModel

class KeysCollection(BaseCollection[KeyModel]):
    items: list[KeyModel]
    errors: Any
