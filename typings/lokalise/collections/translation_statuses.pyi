from lokalise.collections.base_collection import BaseCollection
from lokalise.models.translation_status import TranslationStatusModel

class TranslationStatusesCollection(BaseCollection[TranslationStatusModel]):
    items: list[TranslationStatusModel]
