"""
lokalise.client_methods.glossary_terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for glossary terms.
"""

from typing import Any, Optional, Union

from lokalise.collections.glossary_terms import GlossaryTermsCollection
from lokalise.models.glossary_term import GlossaryTermModel

from .endpoint_provider import EndpointProviderMixin


class GlossaryTermsMethods(EndpointProviderMixin):
    """Glossary term client methods."""

    def glossary_terms(
        self, project_id: str, params: Optional[dict[str, int | str]] = None
    ) -> GlossaryTermsCollection:
        """Fetches all glossary terms for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request parameters
        :return: Collection of glossary terms
        """
        raw_terms = self.get_endpoint("glossary_terms").all(params=params, parent_id=project_id)
        return GlossaryTermsCollection(raw_terms)

    def glossary_term(
        self, project_id: str, glossary_term_id: Union[str, int]
    ) -> GlossaryTermModel:
        """Fetches a glossary term.

        :param str project_id: ID of the project
        :param glossary_term_id: ID of the term to fetch
        :return: Glossary term model
        """
        raw_term = self.get_endpoint("glossary_terms").find(
            parent_id=project_id, resource_id=glossary_term_id
        )
        return GlossaryTermModel(raw_term)

    def create_glossary_terms(
        self, project_id: str, params: Union[dict[str, Any], list[dict[str, Any]]]
    ) -> GlossaryTermsCollection:
        """Creates one or more glossary terms in the project

        :param str project_id: ID of the project
        :param params: Glossary terms parameters
        :type params: list or dict
        :return: Glossary terms collection
        """
        raw_terms = self.get_endpoint("glossary_terms").create(
            params=params, wrapper_attr="terms", parent_id=project_id
        )

        return GlossaryTermsCollection(raw_terms)

    def update_glossary_terms(
        self, project_id: str, params: dict[str, Any]
    ) -> GlossaryTermsCollection:
        """Updates one or more glossary terms.

        :param str project_id: ID of the project
        :param dict params: Glossary terms parameters
        :return: Glossary terms collection
        """
        raw_terms = self.get_endpoint("glossary_terms").update(
            params=params, wrapper_attr="terms", parent_id=project_id
        )
        return GlossaryTermsCollection(raw_terms)

    def delete_glossary_terms(
        self, project_id: str, glossary_terms_ids: list[Union[str, int]]
    ) -> dict[str, Any]:
        """Deletes one or more glossary terms.

        :param str project_id: ID of the project
        :type glossary_terms_id: int or str
        :param list glossary_terms_ids: List of the term IDs to delete
        :return: Delete response
        :rtype dict:
        """
        response = self.get_endpoint("glossary_terms").delete(
            params=glossary_terms_ids, wrapper_attr="terms", parent_id=project_id
        )
        return response
