"""
lokalise.collections.payment_cards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing payment cards collection.
"""

from ..models.payment_card import PaymentCardModel
from .expert_collection import ExpertCollection


class PaymentCardsCollection(ExpertCollection[PaymentCardModel]):
    """Describes payment cards."""

    DATA_KEY = "payment_cards"
    MODEL_KLASS = PaymentCardModel
