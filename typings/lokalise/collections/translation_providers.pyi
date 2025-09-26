from lokalise.collections.base_collection import BaseCollection
from lokalise.models.translation_provider import TranslationProviderModel

class TranslationProvidersCollection(BaseCollection[TranslationProviderModel]):
    items: list[TranslationProviderModel]
