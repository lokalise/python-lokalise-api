"""
lokalise.endpoints.payment_cards_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing payment cards endpoint.
"""

from .base_endpoint import BaseEndpoint


class PaymentCardsEndpoint(BaseEndpoint):
    """Describes payment cards endpoint."""

    PATH = "payment_cards/$parent_id"
