"""
lokalise.client_methods.projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for projects.
"""
from typing import Optional, Dict, Any
from lokalise.models.project import ProjectModel
from lokalise.collections.projects import ProjectsCollection
from .endpoint_provider import EndpointProviderMixin


class ProjectMethods(EndpointProviderMixin):
    """Project client methods.
    """

    def projects(self, params: Optional[Dict] = None) -> ProjectsCollection:
        """Fetches all projects available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of projects
        """
        raw_projects = self.get_endpoint("projects").all(params=params)
        return ProjectsCollection(raw_projects)

    def project(self, project_id: str) -> ProjectModel:
        """Fetches a single project by ID.

        :param str project_id: ID of the project to fetch
        :return: Project model
        """
        raw_project = self.get_endpoint("projects"). \
            find(parent_id=project_id)
        return ProjectModel(raw_project)

    def create_project(self, params: Dict[str, Any]) -> ProjectModel:
        """Creates a new project.

        :param dict params: Project parameters
        :return: Project model
        """
        raw_project = self.get_endpoint("projects").create(params=params)
        return ProjectModel(raw_project)

    def update_project(self, project_id: str,
                       params: Dict[str, Any]) -> ProjectModel:
        """Updates a project.

        :param str project_id: ID of the project to update
        :param dict params: Project parameters
        :return: Project model
        """
        raw_project = self.get_endpoint("projects").\
            update(params=params, parent_id=project_id)
        return ProjectModel(raw_project)

    def empty_project(self, project_id: str) -> Dict:
        """Empties a given project by removing all keys and translations.

        :param str project_id: ID of the project to empty
        :return: Dictionary with the project ID and "keys_deleted" set to True
        :rtype dict:
        """
        return self.get_endpoint("projects").empty(parent_id=project_id)

    def delete_project(self, project_id: str) -> Dict:
        """Deletes a given project.

        :param str project_id: ID of the project to delete
        :return: Dictionary with project ID and "project_deleted" set to True
        :rtype dict:
        """
        return self.get_endpoint("projects").delete(parent_id=project_id)
