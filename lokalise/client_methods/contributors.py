"""
lokalise.client_methods.contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for contributors.
"""
from typing import Optional, Union, Dict, List, Any
from lokalise.models.contributor import ContributorModel
from lokalise.collections.contributors import ContributorsCollection
from .endpoint_provider import EndpointProviderMixin


class ContributorMethods(EndpointProviderMixin):
    """Contributor client methods.
    """

    def contributors(self,
                     project_id: str,
                     params: Optional[Dict[str, Union[int, str]]] = None
                     ) -> ContributorsCollection:
        """Fetches all contributors for the given project.

        :param str project_id: ID of the project to fetch contributors for.
        :param dict params: (optional) Pagination params
        :return: Collection of contributors
        """
        raw_contributors = self.get_endpoint("contributors"). \
            all(parent_id=project_id, params=params)
        return ContributorsCollection(raw_contributors)

    def contributor(self,
                    project_id: str,
                    contributor_id: Union[str, int]) -> ContributorModel:
        """Fetches a single contributor.

        :param str project_id: ID of the project
        :param contributor_id: ID of the contributor to fetch
        :type contributor_id: int or str
        :return: Contributor model
        """
        raw_contributor = self.get_endpoint("contributors"). \
            find(parent_id=project_id, resource_id=contributor_id)
        return ContributorModel(raw_contributor)

    def current_contributor(self,
                            project_id: str) -> ContributorModel:
        """Fetches current contributor (on per-token basis).

        :param str project_id: ID of the project
        :return: Contributor model
        """
        raw_contributor = self.get_endpoint("contributors"). \
            find(parent_id=project_id, resource_id="me")
        return ContributorModel(raw_contributor)

    def create_contributors(self,
                            project_id: str,
                            params: Union[Dict[str, Any], List[Dict]]
                            ) -> ContributorsCollection:
        """Creates one or more contributors inside the project

        :param str project_id: ID of the project
        :param params: Contributors parameters
        :type params: list or dict
        :return: Contributors collection
        """
        raw_contributors = self.get_endpoint("contributors").create(
            params=params,
            wrapper_attr="contributors",
            parent_id=project_id
        )

        return ContributorsCollection(raw_contributors)

    def update_contributor(self,
                           project_id: str,
                           contributor_id: Union[str, int],
                           params: Dict[str, Any]) -> ContributorModel:
        """Updates a single contributor.

        :param str project_id: ID of the project
        :param contributor_id: ID of the contributor to update
        :type contributor_id: int or str
        :param dict params: Update parameters
        :return: Contributor model
        """
        raw_contributor = self.get_endpoint("contributors").update(
            params=params,
            parent_id=project_id,
            resource_id=contributor_id
        )
        return ContributorModel(raw_contributor)

    def delete_contributor(self, project_id: str,
                           contributor_id: Union[str, int]) -> Dict:
        """Deletes a contributor.

        :param str project_id: ID of the project
        :param contributor_id: ID of the contributor to delete
        :type contributor_id: int or str
        :return: Dictionary with project ID and "contributor_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("contributors"). \
            delete(parent_id=project_id, resource_id=contributor_id)
        return response
