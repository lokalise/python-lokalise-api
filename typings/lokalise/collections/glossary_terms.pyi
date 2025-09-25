from lokalise.models.glossary_term import GlossaryTermModel
from lokalise.collections.base_collection import BaseCollection

class GlossaryTermsCollection(BaseCollection[GlossaryTermModel]):
    items: list[GlossaryTermModel]
