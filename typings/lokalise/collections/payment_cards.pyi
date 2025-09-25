from lokalise.models.payment_card import PaymentCardModel
from lokalise.collections.base_collection import BaseCollection

class PaymentCardsCollection(BaseCollection[PaymentCardModel]):
    items: list[PaymentCardModel]
