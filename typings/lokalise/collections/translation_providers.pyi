from lokalise.models.translation_provider import TranslationProviderModel
from lokalise.collections.base_collection import BaseCollection

class TranslationProvidersCollection(BaseCollection[TranslationProviderModel]):
    items: list[TranslationProviderModel]
