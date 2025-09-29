"""
lokalise.collections.glossary_terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing glossary terms collection.
"""

from ..models.glossary_term import GlossaryTermModel
from .base_collection import BaseCollection


class GlossaryTermsCollection(BaseCollection[GlossaryTermModel]):
    """Describes glossary terms."""

    DATA_KEY = "data"
    MODEL_KLASS = GlossaryTermModel
