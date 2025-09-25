"""
lokalise.collections.orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing orders collection.
"""

from ..models.order import OrderModel
from .base_collection import BaseCollection


class OrdersCollection(BaseCollection[OrderModel]):
    """Describes orders."""

    DATA_KEY = "orders"
    MODEL_KLASS = OrderModel
