from typing import TypedDict

from lokalise.models.base_model import BaseModel

class TranslationProviderTier(TypedDict):
    tier_id: int
    title: str

class TranslationProviderPair(TypedDict):
    tier_id: int
    from_lang_iso: str
    from_lang_name: str
    to_lang_iso: str
    to_lang_name: str
    price_per_word: float

class TranslationProviderModel(BaseModel):
    provider_id: int
    name: str
    slug: str
    price_pair_min: float
    website_url: str
    description: str
    tiers: list[TranslationProviderTier]
    pairs: list[TranslationProviderPair]
