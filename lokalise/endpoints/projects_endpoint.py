"""
lokalise.endpoints.projects_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects endpoint.
"""

from .base_endpoint import BaseEndpoint
from .. import request


class ProjectsEndpoint(BaseEndpoint):
    """Describes projects endpoint.
    """
    PATH = "projects/{project_id}"

    def empty(self, project_id):
        """Empties a given project by removing all keys and translations.

        :param project_id: ID of the project to empty
        :rtype dict:
        """
        path = self.PATH.format(
            project_id=project_id
        ).strip('/') + '/empty'
        return request.put(self.client, path)
