"""
lokalise.models.payment_card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing payment card.
"""

from .base_model import BaseModel


class PaymentCardModel(BaseModel):
    """Describes payment card.
    """
    DATA_KEY = 'payment_card'

    ATTRS = [
        'card_id',
        'last4',
        'brand',
        'created_at',
        'created_at_timestamp'
    ]
