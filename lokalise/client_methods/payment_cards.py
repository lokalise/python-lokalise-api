"""
lokalise.client_methods.payment_cards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for payment cards.
"""

from lokalise.collections.payment_cards import PaymentCardsCollection
from lokalise.models.payment_card import PaymentCardModel

from ..mixins.endpoint_provider import EndpointProviderMixin
from lokalise.response import ApiResponse


class PaymentCardMethods(EndpointProviderMixin):
    """Payment card client methods."""

    def payment_cards(self, params: dict[str, str | int] | None = None) -> PaymentCardsCollection:
        """Fetches all payment cards available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of payment cards
        """
        raw_cards = self.get_endpoint("payment_cards").all(params=params)
        return PaymentCardsCollection(raw_cards)

    def payment_card(self, payment_card_id: str | int) -> PaymentCardModel:
        """Fetches a payment card by ID.

        :param payment_card_id: ID of the payment card to fetch
        :type payment_card_id: str or int
        :return: Payment card model
        """
        raw_card = self.get_endpoint("payment_cards").find(parent_id=payment_card_id)
        return PaymentCardModel(raw_card)

    def create_payment_card(self, params: dict[str, int | str]) -> PaymentCardModel:
        """Creates a new payment card.

        :param dict params: Payment card parameters
        :return: Payment card model
        """
        raw_card = self.get_endpoint("payment_cards").create(params=params)
        return PaymentCardModel(raw_card)

    def delete_payment_card(self, payment_card_id: str | int) -> ApiResponse:
        """Deletes a payment card.

        :param payment_card_id: ID of the payment card to delete
        :type payment_card_id: int or str
        :return: Dictionary with card ID and "card_deleted" set to True
        """
        resp = self.get_endpoint("payment_cards").delete(parent_id=payment_card_id)
        return resp
