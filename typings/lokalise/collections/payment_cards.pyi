from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.payment_card import PaymentCardModel

class PaymentCardsCollection(ExpertCollection[PaymentCardModel]):
    items: list[PaymentCardModel]
