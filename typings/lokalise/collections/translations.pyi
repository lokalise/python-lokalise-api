from lokalise.models.translation import TranslationModel
from lokalise.collections.base_collection import BaseCollection

class TranslationsCollection(BaseCollection[TranslationModel]):
    items: list[TranslationModel]
