"""
lokalise.endpoints.orders_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing orders endpoint.
"""
from .base_endpoint import BaseEndpoint


class OrdersEndpoint(BaseEndpoint):
    """Describes orders endpoint.
    """
    PATH = "teams/$parent_id/orders/$resource_id"
