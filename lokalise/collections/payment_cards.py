"""
lokalise.collections.payment_cards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing payment cards collection.
"""

from .base_collection import BaseCollection
from ..models.payment_card import PaymentCardModel


class PaymentCardsCollection(BaseCollection):
    """Describes payment cards.
    """
    DATA_KEY = "payment_cards"
    MODEL_KLASS = PaymentCardModel
