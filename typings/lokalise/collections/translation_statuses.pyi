from lokalise.models.translation_status import TranslationStatusModel
from lokalise.collections.base_collection import BaseCollection

class TranslationStatusesCollection(BaseCollection[TranslationStatusModel]):
    items: list[TranslationStatusModel]
