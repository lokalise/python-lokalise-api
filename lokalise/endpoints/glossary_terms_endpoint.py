"""
lokalise.endpoints.glossary_terms_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing glossary terms endpoint.
"""
from .base_endpoint import BaseEndpoint


class GlossaryTermsEndpoint(BaseEndpoint):
    """Describes glossary terms endpoint.
    """
    PATH = "projects/$parent_id/glossary-terms/$resource_id"
