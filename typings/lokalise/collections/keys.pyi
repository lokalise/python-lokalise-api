from typing import Any

from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.key import KeyModel

class KeysCollection(ExpertCollection[KeyModel]):
    items: list[KeyModel]
    errors: Any
