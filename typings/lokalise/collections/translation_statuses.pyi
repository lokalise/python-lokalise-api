from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.translation_status import TranslationStatusModel

class TranslationStatusesCollection(ExpertCollection[TranslationStatusModel]):
    items: list[TranslationStatusModel]
