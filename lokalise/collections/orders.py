"""
lokalise.collections.orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing orders collection.
"""

from ..models.order import OrderModel
from .expert_collection import ExpertCollection


class OrdersCollection(ExpertCollection[OrderModel]):
    """Describes orders."""

    DATA_KEY = "orders"
    MODEL_KLASS = OrderModel
