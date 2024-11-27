"""
lokalise.client_methods.orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for orders.
"""
from typing import Optional, Union, Dict, Any
from lokalise.models.order import OrderModel
from lokalise.collections.orders import OrdersCollection
from .endpoint_provider import EndpointProviderMixin


class OrderMethods(EndpointProviderMixin):
    """Order client methods.
    """

    def orders(self,
               team_id: Union[int, str],
               params: Optional[Dict[str, Union[str, int]]] = None
               ) -> OrdersCollection:
        """Fetches all orders for the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :param dict params: (optional) Pagination params
        :return: Collection of orders
        """
        raw_orders = self.get_endpoint("orders"). \
            all(parent_id=team_id, params=params)
        return OrdersCollection(raw_orders)

    def order(self,
              team_id: Union[int, str],
              order_id: str
              ) -> OrderModel:
        """Fetches an order for the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :param str order_id: ID of the order
        :return: Order model
        """
        raw_order = self.get_endpoint("orders"). \
            find(parent_id=team_id, resource_id=order_id)
        return OrderModel(raw_order)

    def create_order(self,
                     team_id: Union[int, str],
                     params: Optional[Dict[str, Any]]
                     ) -> OrderModel:
        """Creates a new order inside the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :param dict params: Order parameters
        :return: Order model
        """
        raw_order = self.get_endpoint("orders"). \
            create(parent_id=team_id, params=params)
        return OrderModel(raw_order)
