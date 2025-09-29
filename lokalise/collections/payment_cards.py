"""
lokalise.collections.payment_cards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing payment cards collection.
"""

from ..models.payment_card import PaymentCardModel
from .base_collection import BaseCollection


class PaymentCardsCollection(BaseCollection[PaymentCardModel]):
    """Describes payment cards."""

    DATA_KEY = "payment_cards"
    MODEL_KLASS = PaymentCardModel
