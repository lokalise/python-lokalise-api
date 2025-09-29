from lokalise.collections.base_collection import BaseCollection
from lokalise.models.glossary_term import GlossaryTermModel

class GlossaryTermsCollection(BaseCollection[GlossaryTermModel]):
    items: list[GlossaryTermModel]
