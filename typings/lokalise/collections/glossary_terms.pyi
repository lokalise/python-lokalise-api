from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.glossary_term import GlossaryTermModel

class GlossaryTermsCollection(ExpertCollection[GlossaryTermModel]):
    items: list[GlossaryTermModel]
