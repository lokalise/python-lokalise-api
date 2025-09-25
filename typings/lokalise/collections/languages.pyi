from lokalise.models.language import LanguageModel
from lokalise.collections.base_collection import BaseCollection

class LanguagesCollection(BaseCollection[LanguageModel]):
    items: list[LanguageModel]
