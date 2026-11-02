from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.translation_provider import TranslationProviderModel

class TranslationProvidersCollection(ExpertCollection[TranslationProviderModel]):
    items: list[TranslationProviderModel]
