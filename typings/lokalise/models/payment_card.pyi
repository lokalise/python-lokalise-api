from lokalise.models.base_model import BaseModel

class PaymentCardModel(BaseModel):
    card_id: int
    last4: str
    brand: str
    created_at: str
    created_at_timestamp: int
