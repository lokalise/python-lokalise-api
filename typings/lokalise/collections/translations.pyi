from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.translation import TranslationModel

class TranslationsCollection(ExpertCollection[TranslationModel]):
    items: list[TranslationModel]
