"""
lokalise.endpoints.contributors_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing contributors endpoint.
"""

from .base_endpoint import BaseEndpoint


class ContributorsEndpoint(BaseEndpoint):
    """Describes project contributors endpoint.
    """
    PATH = "projects/{project_id}/contributors/{resource_id}"

    def create(self, params, project_id=None):
        """Creates one or more contributors

        :param str project_id: ID of the project to create resource for
        :param params: Creation parameters
        :type params: list or dict
        :rtype dict:
        """

        # Users may pass params as dict (to create a single contributor)
        # or as a list (to create multiple contributors).
        # Still, the API expects a list in any case
        if isinstance(params, dict):
            params = [params]

        return super().create({"contributors": params}, project_id)
