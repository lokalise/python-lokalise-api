from lokalise.collections.base_collection import BaseCollection
from lokalise.models.order import OrderModel

class OrdersCollection(BaseCollection[OrderModel]):
    items: list[OrderModel]
