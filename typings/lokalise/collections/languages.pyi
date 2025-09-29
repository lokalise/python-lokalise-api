from typing import Any

from lokalise.collections.base_collection import BaseCollection
from lokalise.models.language import LanguageModel

class LanguagesCollection(BaseCollection[LanguageModel]):
    items: list[LanguageModel]
    errors: Any
