from lokalise.collections.base_collection import BaseCollection
from lokalise.models.translation import TranslationModel

class TranslationsCollection(BaseCollection[TranslationModel]):
    items: list[TranslationModel]
