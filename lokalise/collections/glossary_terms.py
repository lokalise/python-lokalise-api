"""
lokalise.collections.glossary_terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing glossary terms collection.
"""

from .base_collection import BaseCollection
from ..models.glossary_term import GlossaryTermModel


class GlossaryTermsCollection(BaseCollection):
    """Describes glossary terms.
    """
    DATA_KEY = "data"
    MODEL_KLASS = GlossaryTermModel
