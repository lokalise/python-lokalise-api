"""
lokalise.endpoints.languages_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing project languages endpoint.
"""

from .base_endpoint import BaseEndpoint


class LanguagesEndpoint(BaseEndpoint):
    """Describes project languages endpoint.
    """
    PATH = "projects/{project_id}/languages/{resource_id}"

    def create(self, params, project_id=None):
        """Creates one or more project languages

        :param params: Creation parameters
        :type params: list or dict
        :param str project_id: ID of the project to create resource for
        :rtype dict:
        """

        # Users may pass params as dict (to create a single language)
        # or as a list (to create multiple languages).
        # Still, the API expects a list in any case
        if isinstance(params, dict):
            params = [params]

        return super().create({"languages": params}, project_id)
