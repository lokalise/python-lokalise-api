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
from .endpoints.system_languages_endpoint import SystemLanguagesEndpoint
from .endpoints.languages_endpoint import LanguagesEndpoint
from .collections.languages import LanguagesCollection
from .models.language import LanguageModel


class Client:
    """Client used to send API requests.

    Usage:

        import lokalise
        client = lokalise.Client('api_token')
        client.projects()
    """

    def __init__(self, token, connect_timeout=None, read_timeout=None):
        """Instantiate a new Lokalise API client.

        :param token: Your Lokalise API token.
        :param connect_timeout: (optional) Server connection timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :param read_timeout: (optional) Server read timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        """
        self.token = token
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout

    def reset_client(self):
        """Resets the API client by setting all options to None.
        """
        self.token = None
        self.connect_timeout = None
        self.read_timeout = None
        self.__clear_endpoint_attrs()

    # === Endpoint methods === #
    def contributors(self, project_id, params=None):
        """Fetches all contributors for the given project.

        :param str project_id: ID of the project to fetch contributors for.
        :param dict params: (optional) Pagination params
        :return: Collection of contributors
        """
        raw_contributors = self.contributors_endpoint(). \
            all(project_id=project_id, params=params)
        return ContributorsCollection(raw_contributors)

    def contributor(self, project_id, contributor_id):
        """Fetches a single contributor.

        :param str project_id: ID of the project
        :param contributor_id: ID of the contributor to fetch
        :type contributor_id: int or str
        :return: Contributor model
        """
        raw_contributor = self.contributors_endpoint(). \
            find(project_id, resource_id=contributor_id)
        return ContributorModel(raw_contributor)

    def create_contributors(self, project_id, params):
        """Creates one or more contributors inside the project

        :param str project_id: ID of the project
        :param params: Contributors parameters
        :type params: list or dict
        :return: Contributors collection
        """
        raw_contributor = self.contributors_endpoint(). \
            create(params, project_id=project_id)

        return ContributorsCollection(raw_contributor)

    def update_contributor(self, project_id, contributor_id, params):
        """Updates a single contributor.

        :param str project_id: ID of the project
        :param contributor_id: ID of the contributor to update
        :type contributor_id: int or str
        :param dict params: Update parameters
        :return: Contributor model
        """
        raw_contributor = self.contributors_endpoint(). \
            update(project_id, params, resource_id=contributor_id)
        return ContributorModel(raw_contributor)

    def delete_contributor(self, project_id, contributor_id):
        """Deletes a contributor.

        :param str project_id: ID of the project
        :param contributor_id: ID of the contributor to delete
        :type contributor_id: int or str
        :return: Dictionary with project ID and "contributor_deleted" set to True
        :rtype dict:
        """
        response = self.contributors_endpoint(). \
            delete(project_id, resource_id=contributor_id)
        return response

    def system_languages(self, params=None):
        """Fetches all languages that Lokalise supports.

        :param dict params: (optional) Pagination params
        :return: Collection of languages
        """
        raw_languages = self.system_languages_endpoint().all(params=params)
        return LanguagesCollection(raw_languages)

    def project_languages(self, project_id, params=None):
        """Fetches all languages for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of languages
        """
        raw_languages = self.languages_endpoint(). \
            all(project_id=project_id, params=params)
        return LanguagesCollection(raw_languages)

    def create_languages(self, project_id, params):
        """Create one or more languages for the given project.

        :param str project_id: ID of the project
        :param params: Language parameters
        :type params: dict or list
        :return: Collection of languages
        """
        raw_languages = self.languages_endpoint(). \
            create(params, project_id=project_id)
        return LanguagesCollection(raw_languages)

    def language(self, project_id, language_id):
        """Fetches a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to fetch
        :return: Language model
        """
        raw_language = self.languages_endpoint(). \
            find(project_id, resource_id=language_id)
        return LanguageModel(raw_language)

    def update_language(self, project_id, language_id, params):
        """Updates a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to update
        :param dict params: Update parameters
        :return: Language model
        """
        raw_language = self.languages_endpoint(). \
            update(project_id, params, resource_id=language_id)
        return LanguageModel(raw_language)

    def delete_language(self, project_id, language_id):
        """Deletes a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to delete
        :return: Dictionary with project ID and "language_deleted" set to True
        :rtype dict:
        """
        response = self.languages_endpoint(). \
            delete(project_id, resource_id=language_id)
        return response

    def projects(self, params=None):
        """Fetches all projects available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of projects
        """
        raw_projects = self.projects_endpoint().all(params=params)
        return ProjectsCollection(raw_projects)

    def project(self, project_id):
        """Fetches a single project by ID.

        :param str project_id: ID of the project to fetch
        :return: Project model
        """
        raw_project = self.projects_endpoint().find(project_id)
        return ProjectModel(raw_project)

    def create_project(self, params):
        """Creates a new project.

        :param dict params: Project parameters
        :return: Project model
        """
        raw_project = self.projects_endpoint().create(params)
        return ProjectModel(raw_project)

    def update_project(self, project_id, params):
        """Updates a project.

        :param str project_id: ID of the project to update
        :param dict params: Project parameters
        :return: Project model
        """
        raw_project = self.projects_endpoint().update(project_id, params)
        return ProjectModel(raw_project)

    def empty_project(self, project_id):
        """Empties a given project by removing all keys and translations.

        :param str project_id: ID of the project to empty
        :return: Dictionary with the project ID and "keys_deleted" set to True
        :rtype dict:
        """
        return self.projects_endpoint().empty(project_id)

    def delete_project(self, project_id):
        """Deletes a given project.

        :param str project_id: ID of the project to empty
        :return: Dictionary with project ID and "project_deleted" set to True
        :rtype dict:
        """
        return self.projects_endpoint().delete(project_id)
    # === End of endpoint methods ===

    # === Endpoint helpers

    def contributors_endpoint(self):
        """Endpoint to work with contributors

        :rtype: endpoints.ContributorsEndpoint
        """
        return self.__fetch_attr('__contributors_endpoint',
                                 lambda: ContributorsEndpoint(self))

    def system_languages_endpoint(self):
        """Endpoint to work with system languages

        :rtype: endpoints.SystemLanguagesEndpoint
        """
        return self.__fetch_attr('__system_languages_endpoint',
                                 lambda: SystemLanguagesEndpoint(self))

    def languages_endpoint(self):
        """Endpoint to work with languages

        :rtype: endpoints.LanguagesEndpoint
        """
        return self.__fetch_attr('__languages_endpoint',
                                 lambda: LanguagesEndpoint(self))

    def projects_endpoint(self):
        """Endpoint to work with contributors

        :rtype: endpoints.ProjectsEndpoint
        """
        return self.__fetch_attr('__projects_endpoint',
                                 lambda: ProjectsEndpoint(self))

    def __fetch_attr(self, attr_name, populator):
        """Searches for the given attribute. Uses populator
        to set the attribute if it cannot be found
        """
        if not hasattr(self, attr_name):
            setattr(self, attr_name, populator())

        return getattr(self, attr_name)

    def __clear_endpoint_attrs(self):
        """Clears all lazily-loaded endpoint attributes
        """
        endpoint_attrs = [a for a in vars(self) if a.endswith('_endpoint')]
        for attr in endpoint_attrs:
            setattr(self, attr, None)
