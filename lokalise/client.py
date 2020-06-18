"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""
from typing import Any, Optional, Union, Dict, Callable, List
import importlib
from lokalise import utils
from .collections.branches import BranchesCollection
from .collections.contributors import ContributorsCollection
from .collections.projects import ProjectsCollection
from .collections.languages import LanguagesCollection
from .models.branch import BranchModel
from .models.contributor import ContributorModel
from .models.project import ProjectModel
from .models.language import LanguageModel


class Client:
    """Client used to send API requests.

    Usage:

        import lokalise
        client = lokalise.Client('api_token')
        client.projects()
    """

    def __init__(
            self,
            token: str,
            connect_timeout: Optional[Union[int, float]] = None,
            read_timeout: Optional[Union[int, float]] = None) -> None:
        """Instantiate a new Lokalise API client.

        :param token: Your Lokalise API token.
        :param connect_timeout: (optional) Server connection timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type connect_timeout: int or float
        :param read_timeout: (optional) Server read timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type read_timeout: int or float
        """
        self.token = token
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout

    def reset_client(self) -> None:
        """Resets the API client by clearing all attributes.
        """
        self.token = ''
        self.connect_timeout = None
        self.read_timeout = None
        self.__clear_endpoint_attrs()

    # === Endpoint methods ===
    def branches(self,
                 project_id: str,
                 params: Optional[Dict[str, Union[int, str]]] = None
                 ) -> BranchesCollection:
        """Fetches all branches for the given project.

        :param str project_id: ID of the project to fetch branches for.
        :param dict params: (optional) Pagination params
        :return: Collection of branches
        """
        raw_branches = self.get_endpoint("branches"). \
            all(project_id=project_id, params=params)
        return BranchesCollection(raw_branches)

    def branch(self,
               project_id: str,
               branch_id: Union[str, int]) -> BranchModel:
        """Fetches a single branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the branch to fetch
        :type branch_id: int or str
        :return: Branch model
        """
        raw_branch = self.get_endpoint("branches"). \
            find(project_id, resource_id=branch_id)
        return BranchModel(raw_branch)

    def create_branch(self,
                      project_id: str,
                      params: Dict[str, str]
                      ) -> BranchModel:
        """Creates a new branch inside the project

        :param str project_id: ID of the project
        :param dict params: Branch parameters
        :return: Branch model
        """
        raw_branch = self.get_endpoint("branches"). \
            create(params, project_id=project_id)

        return BranchModel(raw_branch)

    def update_branch(self,
                      project_id: str,
                      branch_id: Union[str, int],
                      params: Dict[str, str]) -> BranchModel:
        """Updates a branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the branch to update
        :type branch_id: int or str
        :param dict params: Update parameters
        :return: Branch model
        """
        raw_branch = self.get_endpoint("branches"). \
            update(project_id, params, resource_id=branch_id)
        return BranchModel(raw_branch)

    def delete_branch(self, project_id: str,
                      branch_id: Union[str, int]) -> Dict:
        """Deletes a branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the branch to delete
        :type branch_id: int or str
        :return: Dictionary with project ID and "branch_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("branches"). \
            delete(project_id, resource_id=branch_id)
        return response

    def merge_branch(self, project_id: str,
                     branch_id: Union[str, int],
                     params: Optional[Dict[str, Union[str, int]]] = None
                     ) -> Dict:
        """Merges a branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the source branch
        :type branch_id: int or str
        :param dict params: Merge parameters
        :return: Dictionary with project ID, "branch_merged" set to True, and branches info
        :rtype dict:
        """
        response = self.get_endpoint("branches"). \
            merge(project_id, branch_id, params)
        return response

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
            all(project_id=project_id, params=params)
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
            find(project_id, resource_id=contributor_id)
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
        raw_contributors = self.get_endpoint("contributors"). \
            create(params, project_id=project_id)

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
        raw_contributor = self.get_endpoint("contributors"). \
            update(project_id, params, resource_id=contributor_id)
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
            delete(project_id, resource_id=contributor_id)
        return response

    def system_languages(
            self, params: Optional[Dict[str, Union[str, int]]] = None) -> LanguagesCollection:
        """Fetches all languages that Lokalise supports.

        :param dict params: (optional) Pagination params
        :return: Collection of languages
        """
        raw_languages = self.get_endpoint(
            "system_languages").all(params=params)
        return LanguagesCollection(raw_languages)

    def project_languages(self,
                          project_id: str,
                          params: Optional[Dict[str, Union[str, int]]] = None
                          ) -> LanguagesCollection:
        """Fetches all languages for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of languages
        """
        raw_languages = self.get_endpoint("languages"). \
            all(project_id=project_id, params=params)
        return LanguagesCollection(raw_languages)

    def create_languages(self,
                         project_id: str,
                         params: Dict[str, Any]) -> LanguagesCollection:
        """Create one or more languages for the given project.

        :param str project_id: ID of the project
        :param params: Language parameters
        :type params: dict or list
        :return: Collection of languages
        """
        raw_languages = self.get_endpoint("languages"). \
            create(params, project_id=project_id)
        return LanguagesCollection(raw_languages)

    def language(self,
                 project_id: str,
                 language_id: Union[str, int]) -> LanguageModel:
        """Fetches a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to fetch
        :return: Language model
        """
        raw_language = self.get_endpoint("languages"). \
            find(project_id, resource_id=language_id)
        return LanguageModel(raw_language)

    def update_language(self,
                        project_id: str,
                        language_id: Union[str, int],
                        params: Dict[str, Any]) -> LanguageModel:
        """Updates a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to update
        :param dict params: Update parameters
        :return: Language model
        """
        raw_language = self.get_endpoint("languages"). \
            update(project_id, params, resource_id=language_id)
        return LanguageModel(raw_language)

    def delete_language(self, project_id: str,
                        language_id: Union[str, int]) -> Dict:
        """Deletes a project language.

        :param str project_id: ID of the project
        :param language_id: ID of the language to delete
        :return: Dictionary with project ID and "language_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("languages"). \
            delete(project_id, resource_id=language_id)
        return response

    def projects(self, params: Optional[str] = None) -> ProjectsCollection:
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
        raw_project = self.get_endpoint("projects").find(project_id)
        return ProjectModel(raw_project)

    def create_project(self, params: Dict[str, Any]) -> ProjectModel:
        """Creates a new project.

        :param dict params: Project parameters
        :return: Project model
        """
        raw_project = self.get_endpoint("projects").create(params)
        return ProjectModel(raw_project)

    def update_project(self, project_id: str,
                       params: Dict[str, Any]) -> ProjectModel:
        """Updates a project.

        :param str project_id: ID of the project to update
        :param dict params: Project parameters
        :return: Project model
        """
        raw_project = self.get_endpoint("projects").update(project_id, params)
        return ProjectModel(raw_project)

    def empty_project(self, project_id: str) -> Dict:
        """Empties a given project by removing all keys and translations.

        :param str project_id: ID of the project to empty
        :return: Dictionary with the project ID and "keys_deleted" set to True
        :rtype dict:
        """
        return self.get_endpoint("projects").empty(project_id)

    def delete_project(self, project_id: str) -> Dict:
        """Deletes a given project.

        :param str project_id: ID of the project to empty
        :return: Dictionary with project ID and "project_deleted" set to True
        :rtype dict:
        """
        return self.get_endpoint("projects").delete(project_id)
    # === End of endpoint methods ===

    # === Endpoint helpers
    def get_endpoint(self, name: str) -> Any:
        """Lazily loads an endpoint with a given name and stores it
        under a specific instance attribute. For example, if the `name`
        is "projects", then it will load .endpoints.projects_endpoint module
        and then set attribute like this:
            self.__projects_endpoint = ProjectsEndpoint(self)

        :param str name: Endpoint name to load
        """
        endpoint_name = name + "_endpoint"
        camelized_name = utils.snake_to_camel(endpoint_name)
        # Dynamically load the necessary endpoint module
        module = importlib.import_module(
            f".endpoints.{endpoint_name}", package='lokalise')
        # Find endpoint class in the module
        endpoint_klass = getattr(module, camelized_name)
        return self.__fetch_attr(f"__{endpoint_name}",
                                 lambda: endpoint_klass(self))

    def __fetch_attr(self, attr_name: str, populator: Callable) -> Any:
        """Searches for the given attribute. Uses populator
        to set the attribute if it cannot be found. Used to lazy-load
        endpoints.
        """
        if not hasattr(self, attr_name):
            setattr(self, attr_name, populator())

        return getattr(self, attr_name)

    def __clear_endpoint_attrs(self) -> None:
        """Clears all lazily-loaded endpoint attributes
        """
        endpoint_attrs = [a for a in vars(self) if a.endswith('_endpoint')]
        for attr in endpoint_attrs:
            setattr(self, attr, None)
