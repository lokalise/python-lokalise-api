from typing import Any

from lokalise.models.base_model import BaseModel

class TranslationProviderModel(BaseModel):
    provider_id: int
    name: str
    slug: str
    price_pair_min: float
    website_url: str
    description: str
    tiers: list[dict[str, Any]]
    pairs: list[dict[str, Any]]
