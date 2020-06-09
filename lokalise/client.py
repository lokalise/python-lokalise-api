"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""

from .endpoints.projects_endpoint import ProjectsEndpoint
from .collections.projects import ProjectsCollection
from .models.project import ProjectModel
from .endpoints.contributors_endpoint import ContributorsEndpoint
from .collections.contributors import ContributorsCollection
from .models.contributor import ContributorModel


class Client:
    def __init__(self, token, connect_timeout=None, read_timeout=None):
        """Instantiate a new Lokalise API client.
        Args:
          token (str):
            Your Lokalise API token.
        """
        self.token = token
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout

    def reset_client(self):
        self.token = None
        self.connect_timeout = None
        self.read_timeout = None
        self.__clear_endpoint_attrs()

    def projects(self, params={}):
        raw_projects = self.projects_endpoint().all(params=params)
        return ProjectsCollection(raw_projects)

    def project(self, project_id):
        raw_project = self.projects_endpoint().find(project_id)
        return ProjectModel(raw_project)

    def contributors(self, project_id, params={}):
        raw_contributors = self.contributors_endpoint(). \
            all(project_id=project_id, params=params)
        return ContributorsCollection(raw_contributors)

    def contributor(self, project_id, contributor_id):
        raw_contributor = self.contributors_endpoint(). \
            find(project_id, resource_id=contributor_id)
        return ContributorModel(raw_contributor)

    def contributors_endpoint(self):
        return self.__fetch_attr('__contributors_endpoint',
                                 lambda: ContributorsEndpoint(self))

    def projects_endpoint(self):
        return self.__fetch_attr('__projects_endpoint',
                                 lambda: ProjectsEndpoint(self))

    def __fetch_attr(self, attr_name, populator):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, populator())

        return getattr(self, attr_name)

    def __clear_endpoint_attrs(self):
        endpoint_attrs = [a for a in vars(self) if a.endswith('_endpoint')]
        for attr in endpoint_attrs:
            setattr(self, attr, None)
