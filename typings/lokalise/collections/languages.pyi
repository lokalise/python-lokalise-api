from typing import Any

from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.language import LanguageModel

class LanguagesCollection(ExpertCollection[LanguageModel]):
    items: list[LanguageModel]
    errors: Any
