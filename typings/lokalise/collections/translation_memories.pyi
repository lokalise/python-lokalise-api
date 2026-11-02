from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.translation_memory import TranslationMemoryModel

class TranslationMemoriesCollection(ExpertCollection[TranslationMemoryModel]):
    items: list[TranslationMemoryModel]
