"""
lokalise.collections.orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing orders collection.
"""

from .base_collection import BaseCollection
from ..models.order import OrderModel


class OrdersCollection(BaseCollection):
    """Describes orders.
    """
    DATA_KEY = "orders"
    MODEL_KLASS = OrderModel
