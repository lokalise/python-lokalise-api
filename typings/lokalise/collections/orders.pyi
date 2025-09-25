from lokalise.models.order import OrderModel
from lokalise.collections.base_collection import BaseCollection

class OrdersCollection(BaseCollection[OrderModel]):
    items: list[OrderModel]
