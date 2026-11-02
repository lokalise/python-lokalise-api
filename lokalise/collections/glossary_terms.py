"""
lokalise.collections.glossary_terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing glossary terms collection.
"""

from ..models.glossary_term import GlossaryTermModel
from .expert_collection import ExpertCollection


class GlossaryTermsCollection(ExpertCollection[GlossaryTermModel]):
    """Describes glossary terms."""

    DATA_KEY = "data"
    MODEL_KLASS = GlossaryTermModel
