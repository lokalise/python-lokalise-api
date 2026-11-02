from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.order import OrderModel

class OrdersCollection(ExpertCollection[OrderModel]):
    items: list[OrderModel]
