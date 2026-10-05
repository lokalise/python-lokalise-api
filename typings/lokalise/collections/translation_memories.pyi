from lokalise.collections.base_collection import BaseCollection
from lokalise.models.translation_memory import TranslationMemoryModel

class TranslationMemoriesCollection(BaseCollection[TranslationMemoryModel]):
    items: list[TranslationMemoryModel]
