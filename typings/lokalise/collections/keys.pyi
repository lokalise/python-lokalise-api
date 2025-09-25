from lokalise.models.key import KeyModel
from lokalise.collections.base_collection import BaseCollection

class KeysCollection(BaseCollection[KeyModel]):
    items: list[KeyModel]
