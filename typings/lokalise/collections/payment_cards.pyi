from lokalise.collections.base_collection import BaseCollection
from lokalise.models.payment_card import PaymentCardModel

class PaymentCardsCollection(BaseCollection[PaymentCardModel]):
    items: list[PaymentCardModel]
