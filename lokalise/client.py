"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""
from typing import Any, Optional, Union, Dict, Callable, List
import importlib
from lokalise.utils import snake_to_camel
from .base_client import BaseClient
from .collections.branches import BranchesCollection
from .collections.comments import CommentsCollection
from .collections.contributors import ContributorsCollection
from .collections.files import FilesCollection
from .collections.keys import KeysCollection
from .collections.languages import LanguagesCollection
from .collections.orders import OrdersCollection
from .collections.payment_cards import PaymentCardsCollection
from .collections.projects import ProjectsCollection
from .collections.queued_processes import QueuedProcessesCollection
from .collections.snapshots import SnapshotsCollection
from .collections.screenshots import ScreenshotsCollection
from .collections.segments import SegmentsCollection
from .collections.tasks import TasksCollection
from .collections.teams import TeamsCollection
from .collections.team_users import TeamUsersCollection
from .collections.team_user_groups import TeamUserGroupsCollection
from .collections.translations import TranslationsCollection
from .collections.translation_providers import TranslationProvidersCollection
from .collections.translation_statuses import TranslationStatusesCollection
from .collections.webhooks import WebhooksCollection
from .models.branch import BranchModel
from .models.comment import CommentModel
from .models.contributor import ContributorModel
from .models.jwt import JwtModel
from .models.key import KeyModel
from .models.language import LanguageModel
from .models.order import OrderModel
from .models.payment_card import PaymentCardModel
from .models.project import ProjectModel
from .models.queued_process import QueuedProcessModel
from .models.snapshot import SnapshotModel
from .models.screenshot import ScreenshotModel
from .models.segment import SegmentModel
from .models.task import TaskModel
from .models.team_user import TeamUserModel
from .models.team_user_group import TeamUserGroupModel
from .models.translation import TranslationModel
from .models.translation_provider import TranslationProviderModel
from .models.translation_status import TranslationStatusModel
from .models.webhook import WebhookModel
from .models.team_user_billing_details import TeamUsersBillingDetailsModel


class Client(BaseClient):
    """Client used to send API requests.

    Usage:

        import lokalise
        client = lokalise.Client('api_token')
        client.projects()
    """

    def reset_client(self) -> None:
        """Resets the API client by clearing all attributes.
        """
        self.token = ''
        self.connect_timeout = None
        self.read_timeout = None
        self.enable_compression = False
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
            all(parent_id=project_id, params=params)
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
            find(parent_id=project_id, resource_id=branch_id)
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
            create(params=params, parent_id=project_id)

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
            update(params=params, parent_id=project_id, resource_id=branch_id)
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
            delete(parent_id=project_id, resource_id=branch_id)
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
            merge(params=params, parent_id=project_id, resource_id=branch_id)
        response['branch'] = BranchModel(response['branch'])
        response['target_branch'] = BranchModel(response['target_branch'])
        return response

    def project_comments(self,
                         project_id: str,
                         params: Optional[Dict[str, Union[int, str]]] = None
                         ) -> CommentsCollection:
        """Fetches all comments for the given project.

        :param str project_id: ID of the project to fetch comments for.
        :param dict params: (optional) Pagination params
        :return: Collection of comments
        """
        raw_comments = self.get_endpoint("project_comments"). \
            all(parent_id=project_id, params=params)
        return CommentsCollection(raw_comments)

    def key_comments(self,
                     project_id: str,
                     key_id: Union[str, int],
                     params: Optional[Dict[str, Union[int, str]]] = None
                     ) -> CommentsCollection:
        """Fetches all comments for the given key inside a project.

        :param str project_id: ID of the project
        :param key_id: ID of key to fetch comments for
        :type key_id: int or str
        :param dict params: (optional) Pagination params
        :return: Collection of comments
        """
        raw_comments = self.get_endpoint("key_comments"). \
            all(params=params, parent_id=project_id, resource_id=key_id)
        return CommentsCollection(raw_comments)

    def key_comment(self,
                    project_id: str,
                    key_id: Union[str, int],
                    comment_id: Union[str, int]
                    ) -> CommentModel:
        """Fetches a single comment for a given key.

        :param str project_id: ID of the project
        :param key_id: ID of key to fetch comments for
        :type key_id: int or str
        :param comment_id: Comment identifier to fetch
        :type comment_id: int or str
        :return: Comment model
        """
        raw_comment = self.get_endpoint("key_comments").find(
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=comment_id
        )
        return CommentModel(raw_comment)

    def create_key_comments(self,
                            project_id: str,
                            key_id: Union[str, int],
                            params: Union[List[Dict], Dict[str, str]]
                            ) -> CommentsCollection:
        """Creates one or more comments for the given key.

        :param str project_id: ID of the project
        :param key_id: ID of key to create comments for
        :type key_id: int or str
        :param params: Comment parameters
        :type params: list or dict
        :return: Collection of comments
        """
        raw_comments = self.get_endpoint("key_comments").create(
            params=params,
            wrapper_attr="comments",
            parent_id=project_id,
            resource_id=key_id
        )
        return CommentsCollection(raw_comments)

    def delete_key_comment(self,
                           project_id: str,
                           key_id: Union[str, int],
                           comment_id: Union[str, int]
                           ) -> Dict:
        """Deletes a given key comment.

        :param str project_id: ID of the project
        :param key_id: ID of key to delete comment for.
        :type key_id: int or str
        :param comment_id: Comment to delete
        :type comment_id: int or str
        :return: Dictionary with project ID and "comment_deleted" set to True
        """
        response = self.get_endpoint("key_comments").delete(
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=comment_id
        )
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

    def files(self,
              project_id: str,
              params: Optional[Dict[str, Union[int, str]]] = None
              ) -> FilesCollection:
        """Fetches all files for the given project.

        :param str project_id: ID of the project to fetch files for.
        :param dict params: (optional) Pagination params
        :return: Collection of files
        """
        raw_files = self.get_endpoint("files"). \
            all(parent_id=project_id, params=params)
        return FilesCollection(raw_files)

    def upload_file(self, project_id: str,
                    params: Dict[str, Any]) -> QueuedProcessModel:
        """Uploads a file to the given project.

        :param str project_id: ID of the project to upload file to
        :param dict params: Upload params
        :return: Queued process model
        """
        raw_process = self.get_endpoint("files"). \
            upload(params=params, parent_id=project_id)
        return QueuedProcessModel(raw_process)

    def download_files(self, project_id: str,
                       params: Dict[str, Any]) -> Dict:
        """Downloads files from the given project.

        :param str project_id: ID of the project to download from
        :param dict params: Download params
        :return: Dictionary with project ID and a bundle URL
        """
        response = self.get_endpoint("files"). \
            download(params=params, parent_id=project_id)
        return response

    def delete_file(self, project_id: str,
                    file_id: Union[str, int]) -> Dict:
        """Deletes a file and it's associated keys from the project.
        File __unassigned__ cannot be deleted.
        This endpoint does not support "software localization" projects.

        :param str project_id: ID of the project
        :param file_id: ID of the file to delete
        :return: Dictionary with project ID and "file_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("files"). \
            delete(parent_id=project_id, resource_id=file_id)
        return response

    def jwt(self) -> JwtModel:
        """Fetches OTA JWT.

        :return: JWT model
        """
        raw_jwt = self.get_endpoint("jwt").find()
        return JwtModel(raw_jwt)

    def keys(self,
             project_id: str,
             params: Optional[Dict[str, Any]] = None
             ) -> KeysCollection:
        """Fetches all keys for the given project.

        :param str project_id: ID of the project
        :param dict params: Request parameters
        :return: Collection of keys
        """
        raw_keys = self.get_endpoint("keys"). \
            all(parent_id=project_id, params=params)
        return KeysCollection(raw_keys)

    def create_keys(self,
                    project_id: str,
                    params: Union[Dict[str, Any], List[Dict]]
                    ) -> KeysCollection:
        """Creates one or more keys inside the project

        :param str project_id: ID of the project
        :param params: Keys parameters
        :type params: list or dict
        :return: Keys collection
        """
        raw_keys = self.get_endpoint("keys"). \
            create(params=params, wrapper_attr="keys", parent_id=project_id)

        return KeysCollection(raw_keys)

    def key(self,
            project_id: str,
            key_id: Union[str, int],
            params: Optional[Dict[str, Any]] = None) -> KeyModel:
        """Fetches a translation key.

        :param str project_id: ID of the project
        :param key_id: ID of the key to fetch
        :param dict params: Request parameters
        :return: Key model
        """
        raw_key = self.get_endpoint("keys"). \
            find(params=params, parent_id=project_id, resource_id=key_id)
        return KeyModel(raw_key)

    def update_key(self,
                   project_id: str,
                   key_id: Union[str, int],
                   params: Optional[Dict[str, Any]] = None) -> KeyModel:
        """Updates a translation key.

        :param str project_id: ID of the project
        :param key_id: ID of the key to update
        :param dict params: Request parameters
        :return: Key model
        """
        raw_key = self.get_endpoint("keys"). \
            update(params=params, parent_id=project_id, resource_id=key_id)
        return KeyModel(raw_key)

    def update_keys(self,
                    project_id: str,
                    params: Dict[str, Any]) -> KeysCollection:
        """Updates translation keys in bulk.

        :param str project_id: ID of the project
        :param dict params: Key parameters
        :return: Key collection
        """
        raw_keys = self.get_endpoint("keys"). \
            update(params=params, wrapper_attr="keys", parent_id=project_id)
        return KeysCollection(raw_keys)

    def delete_key(self, project_id: str,
                   key_id: Union[str, int]) -> Dict:
        """Deletes a key.

        :param str project_id: ID of the project
        :param key_id: ID of the key to delete
        :type key_id: int or str
        :return: Dictionary with project ID and "key_removed" set to True
        :rtype dict:
        """
        response = self.get_endpoint("keys"). \
            delete(parent_id=project_id, resource_id=key_id)
        return response

    def delete_keys(self, project_id: str,
                    key_ids: List[Union[str, int]]) -> Dict:
        """Deletes keys in bulk.

        :param str project_id: ID of the project
        :type key_id: int or str
        :param list key_ids: List of the key identifiers to delete
        :return: Dictionary with project ID and "keys_removed" set to True
        :rtype dict:
        """
        response = self.get_endpoint("keys"). \
            delete(params=key_ids, wrapper_attr="keys", parent_id=project_id)
        return response

    def system_languages(self,
                         params: Optional[Dict[str, Union[str, int]]] = None
                         ) -> LanguagesCollection:
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
            all(parent_id=project_id, params=params)
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
        raw_languages = self.get_endpoint("languages").create(
            params=params,
            wrapper_attr="languages",
            parent_id=project_id
        )
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
            find(parent_id=project_id, resource_id=language_id)
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
        raw_language = self.get_endpoint("languages").update(
            params=params,
            parent_id=project_id,
            resource_id=language_id
        )
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
            delete(parent_id=project_id, resource_id=language_id)
        return response

    def orders(self,
               team_id: Union[int, str],
               params: Optional[Dict[str, Union[str, int]]] = None
               ) -> OrdersCollection:
        """Fetches all orders for the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :param dict params: (optional) Pagination params
        :return: Collection of orders
        """
        raw_orders = self.get_endpoint("orders"). \
            all(parent_id=team_id, params=params)
        return OrdersCollection(raw_orders)

    def order(self,
              team_id: Union[int, str],
              order_id: str
              ) -> OrderModel:
        """Fetches an order for the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :param str order_id: ID of the order
        :return: Order model
        """
        raw_order = self.get_endpoint("orders"). \
            find(parent_id=team_id, resource_id=order_id)
        return OrderModel(raw_order)

    def create_order(self,
                     team_id: Union[int, str],
                     params: Optional[Dict[str, Any]]
                     ) -> OrderModel:
        """Creates a new order inside the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :param dict params: Order parameters
        :return: Order model
        """
        raw_order = self.get_endpoint("orders"). \
            create(parent_id=team_id, params=params)
        return OrderModel(raw_order)

    def payment_cards(self,
                      params: Optional[Dict] = None) -> PaymentCardsCollection:
        """Fetches all payment cards available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of payment cards
        """
        raw_cards = self.get_endpoint("payment_cards").all(params=params)
        return PaymentCardsCollection(raw_cards)

    def payment_card(self,
                     payment_card_id: Union[str, int]) -> PaymentCardModel:
        """Fetches a payment card by ID.

        :param payment_card_id: ID of the payment card to fetch
        :type payment_card_id: str or int
        :return: Payment card model
        """
        raw_card = self.get_endpoint("payment_cards"). \
            find(parent_id=payment_card_id)
        return PaymentCardModel(raw_card)

    def create_payment_card(self, params: Dict[str, Union[int, str]]
                            ) -> PaymentCardModel:
        """Creates a new payment card.

        :param dict params: Payment card parameters
        :return: Payment card model
        """
        raw_card = self.get_endpoint("payment_cards").create(params=params)
        return PaymentCardModel(raw_card)

    def delete_payment_card(self, payment_card_id: Union[str, int]) -> Dict:
        """Deletes a payment card.

        :param payment_card_id: ID of the payment card to delete
        :type payment_card_id: int or str
        :return: Dictionary with card ID and "card_deleted" set to True
        :rtype dict:
        """
        resp = self.get_endpoint("payment_cards"). \
            delete(parent_id=payment_card_id)
        return resp

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

    def queued_processes(self, project_id: str) -> QueuedProcessesCollection:
        """Fetches all queued processes for the given project.

        :param str project_id: ID of the project
        :return: Collection of queued processes
        """
        raw_processes = self.get_endpoint("queued_processes"). \
            all(parent_id=project_id)
        return QueuedProcessesCollection(raw_processes)

    def queued_process(self,
                       project_id: str,
                       queued_process_id: Union[str,
                                                int]) -> QueuedProcessModel:
        """Fetches a queued process.

        :param str project_id: ID of the project
        :param queued_process_id: ID of the process to fetch
        :type queued_process_id: int or str
        :return: Queued process model
        """
        raw_process = self.get_endpoint("queued_processes"). \
            find(parent_id=project_id, resource_id=queued_process_id)
        return QueuedProcessModel(raw_process)

    def snapshots(self, project_id: str,
                  params: Optional[Dict] = None) -> SnapshotsCollection:
        """Fetches all snapshots for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of snapshots
        """
        raw_snapshots = self.get_endpoint("snapshots"). \
            all(params=params, parent_id=project_id)
        return SnapshotsCollection(raw_snapshots)

    def create_snapshot(self, project_id: str,
                        params: Optional[Dict[str, str]] = None
                        ) -> SnapshotModel:
        """Creates a snapshot of the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request params
        :return: Snapshot model
        """
        raw_snapshot = self.get_endpoint("snapshots"). \
            create(params=params, parent_id=project_id)
        return SnapshotModel(raw_snapshot)

    def restore_snapshot(self,
                         project_id: str,
                         snapshot_id: Union[str, int]) -> ProjectModel:
        """Restores a snapshot of the given project by producing a new project.

        :param str project_id: ID of the project
        :param queued_process_id: ID of the snapshot to restore
        :type snapshot_id: int or str
        :return: Snapshot model
        """
        new_project = self.get_endpoint("snapshots"). \
            create(parent_id=project_id, resource_id=snapshot_id)
        return ProjectModel(new_project)

    def delete_snapshot(self, project_id: str,
                        snapshot_id: Union[str, int]) -> Dict:
        """Deletes a project snapshot.

        :param str project_id: ID of the project
        :param snapshot_id: ID of the snapshot to delete
        :return: Dictionary with project ID and "snapshot_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("snapshots"). \
            delete(parent_id=project_id, resource_id=snapshot_id)
        return response

    def screenshots(self, project_id: str,
                    params: Optional[Dict] = None) -> ScreenshotsCollection:
        """Fetches all screenshots for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of screenshots
        """
        raw_screenshots = self.get_endpoint("screenshots"). \
            all(params=params, parent_id=project_id)
        return ScreenshotsCollection(raw_screenshots)

    def screenshot(self,
                   project_id: str,
                   screenshot_id: Union[str, int]) -> ScreenshotModel:
        """Fetches a screenshot.

        :param str project_id: ID of the project
        :param screenshot_id: ID of the screenshot to fetch
        :type screenshot_id: int or str
        :return: Screenshot model
        """
        screenshot = self.get_endpoint("screenshots"). \
            find(parent_id=project_id, resource_id=screenshot_id)
        return ScreenshotModel(screenshot)

    def create_screenshots(self, project_id: str,
                           params: Union[List[Dict], Dict[str, Any]]
                           ) -> ScreenshotsCollection:
        """Creates one or more screenshots in the given project.

        :param str project_id: ID of the project
        :param params: Screenshots parameters
        :type params: dict or list
        :return: Collection of screenshots
        """
        raw_screenshots = self.get_endpoint("screenshots").create(
            params=params,
            wrapper_attr="screenshots",
            parent_id=project_id
        )
        return ScreenshotsCollection(raw_screenshots)

    def update_screenshot(self,
                          project_id: str,
                          screenshot_id: Union[str, int],
                          params: Optional[Dict[str, Any]] = None
                          ) -> ScreenshotModel:
        """Updates a screenshot.

        :param str project_id: ID of the project
        :param screenshot_id: ID of the screenshot to update
        :type screenshot_id: int or str
        :param dict params: Screenshots parameters
        :return: Screenshot model
        """
        screenshot = self.get_endpoint("screenshots").update(
            params=params,
            parent_id=project_id,
            resource_id=screenshot_id
        )
        return ScreenshotModel(screenshot)

    def delete_screenshot(self,
                          project_id: str,
                          screenshot_id: Union[str, int]) -> Dict:
        """Deletes a screenshot.

        :param str project_id: ID of the project
        :param screenshot_id: ID of the screenshot to delete
        :type screenshot_id: int or str
        :return: Dictionary with the project ID and "screenshot_deleted": True
        """
        response = self.get_endpoint("screenshots"). \
            delete(parent_id=project_id, resource_id=screenshot_id)
        return response

    def segments(self, project_id: str, key_id: Union[str, int], lang_iso: str,
                 params: Optional[Dict] = None) -> SegmentsCollection:
        """Fetches all segments for the given key and language inside a project.

        :param str project_id: ID of the project
        :param str key_id: ID of the key
        :type key_id: int or str
        :param str lang_iso: Language ISO code
        :param dict params: (optional) Additional params
        :return: Collection of segments
        """
        raw_segments = self.get_endpoint("segments").all(
            params=params,
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=lang_iso)
        return SegmentsCollection(raw_segments)

    # pylint: disable=too-many-arguments
    def segment(self,
                project_id: str,
                key_id: Union[str, int],
                lang_iso: str,
                segment_number: Union[str, int],
                params: Optional[Dict] = None) -> SegmentModel:
        """Fetches a segment for the given key and language inside a project.

        :param str project_id: ID of the project
        :param str key_id: ID of the key
        :type key_id: int or str
        :param str lang_iso: Language ISO code
        :param str segment_number: Number of the segment
        :type segment_number: int or str
        :param dict params: (optional) Additional params
        :return: Segment model
        """
        raw_segment = self.get_endpoint("segments").find(
            params=params,
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=f"{lang_iso}/{segment_number}")
        return SegmentModel(raw_segment)

    def update_segment(self,
                       project_id: str,
                       key_id: Union[str, int],
                       lang_iso: str,
                       segment_number: Union[str, int],
                       params: Dict) -> SegmentModel:
        """Updates a segment.

        :param str project_id: ID of the project
        :param str key_id: ID of the key
        :type key_id: int or str
        :param str lang_iso: Language ISO code
        :param str segment_number: Number of the segment
        :type segment_number: int or str
        :param dict params: New segment attributes
        :return: Segment model
        """
        raw_segment = self.get_endpoint("segments").update(
            params=params,
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=f"{lang_iso}/{segment_number}")
        return SegmentModel(raw_segment)
    # pylint: enable=too-many-arguments

    def tasks(self, project_id: str,
              params: Optional[Dict] = None) -> TasksCollection:
        """Fetches all tasks for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request parameters
        :return: Collection of tasks
        """
        raw_tasks = self.get_endpoint("tasks"). \
            all(params=params, parent_id=project_id)
        return TasksCollection(raw_tasks)

    def task(self,
             project_id: str,
             task_id: Union[str, int]) -> TaskModel:
        """Fetches a task.

        :param str project_id: ID of the project
        :param task_id: ID of the task to fetch
        :type task_id: int or str
        :return: Task model
        """
        raw_task = self.get_endpoint("tasks"). \
            find(parent_id=project_id, resource_id=task_id)
        return TaskModel(raw_task)

    def create_task(self, project_id: str,
                    params: Dict[str, Any]) -> TaskModel:
        """Creates a task in the given project.

        :param str project_id: ID of the project
        :param dict params: Task parameters
        :return: Task model
        """
        raw_task = self.get_endpoint("tasks"). \
            create(params=params, parent_id=project_id)
        return TaskModel(raw_task)

    def update_task(self,
                    project_id: str,
                    task_id: Union[str, int],
                    params: Optional[Dict[str, Any]] = None
                    ) -> TaskModel:
        """Updates a task.

        :param str project_id: ID of the project
        :param task_id: ID of the task to update
        :type task_id: int or str
        :param dict params: Task parameters
        :return: Task model
        """
        raw_task = self.get_endpoint("tasks"). \
            update(params=params, parent_id=project_id, resource_id=task_id)
        return TaskModel(raw_task)

    def delete_task(self,
                    project_id: str,
                    task_id: Union[str, int]) -> Dict:
        """Deletes a task.

        :param str project_id: ID of the project
        :param task_id: ID of the task to delete
        :type task_id: int or str
        :return: Dictionary with the project ID and "task_deleted": True
        """
        response = self.get_endpoint("tasks"). \
            delete(parent_id=project_id, resource_id=task_id)
        return response

    def teams(self, params: Optional[Dict] = None) -> TeamsCollection:
        """Fetches all teams available to the currently authorized user
        (identified by the API token).

        :param dict params: (optional) Pagination params
        :return: Collection of teams
        """
        raw_teams = self.get_endpoint("teams").all(params=params)
        return TeamsCollection(raw_teams)

    def team_users(self, team_id: Union[str, int],
                   params: Optional[Dict] = None) -> TeamUsersCollection:
        """Fetches all team users.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: (optional) Pagination parameters
        :return: Collection of team users
        """
        raw_team_users = self.get_endpoint("team_users"). \
            all(params=params, parent_id=team_id)
        return TeamUsersCollection(raw_team_users)

    def team_user(self, team_id: Union[str, int],
                  team_user_id: Union[str, int]) -> TeamUserModel:
        """Fetches a team user.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_id: ID of the team user to fetch
        :type team_user_id: str or int
        :return: Team user model
        """
        raw_team_user = self.get_endpoint("team_users"). \
            find(parent_id=team_id, resource_id=team_user_id)
        return TeamUserModel(raw_team_user)

    def update_team_user(self, team_id: Union[str, int],
                         team_user_id: Union[str, int],
                         params: Optional[Dict] = None) -> TeamUserModel:
        """Updates a team user.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_id: ID of the team user to update
        :type team_user_id: str or int
        :param dict params: (optional) Team user parameters
        :return: Team user model
        """
        raw_team_user = self.get_endpoint("team_users"). \
            update(params=params, parent_id=team_id, resource_id=team_user_id)
        return TeamUserModel(raw_team_user)

    def delete_team_user(self, team_id: Union[str, int],
                         team_user_id: Union[str, int]) -> Dict:
        """Deletes a team user.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_id: ID of the team user to delete
        :type team_user_id: str or int
        :return: Dict with the team ID and `team_user_deleted` set to True
        """
        response = self.get_endpoint("team_users"). \
            delete(parent_id=team_id, resource_id=team_user_id)
        return response

    def team_user_groups(self, team_id: Union[str, int],
                         params: Optional[Dict] = None
                         ) -> TeamUserGroupsCollection:
        """Fetches all team user groups.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: (optional) Pagination parameters
        :return: Collection of team user groups
        """
        raw_groups = self.get_endpoint("team_user_groups"). \
            all(params=params, parent_id=team_id)
        return TeamUserGroupsCollection(raw_groups)

    def team_user_group(self, team_id: Union[str, int],
                        team_user_group_id: Union[str, int]
                        ) -> TeamUserGroupModel:
        """Fetches a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to fetch
        :type team_user_group_id: str or int
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups"). \
            find(parent_id=team_id, resource_id=team_user_group_id)
        return TeamUserGroupModel(raw_group)

    def create_team_user_group(self, team_id: Union[str, int],
                               params: Dict[str, Any]
                               ) -> TeamUserGroupModel:
        """Fetches a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: Team user group parameters
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups"). \
            create(params=params, parent_id=team_id)
        return TeamUserGroupModel(raw_group)

    def update_team_user_group(self, team_id: Union[str, int],
                               team_user_group_id: Union[str, int],
                               params: Dict[str, Any]
                               ) -> TeamUserGroupModel:
        """Updates a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to update
        :type team_user_group_id: str or int
        :param dict params: Team user group parameters
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").update(
            params=params,
            parent_id=team_id,
            resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def delete_team_user_group(self, team_id: Union[str, int],
                               team_user_group_id: Union[str, int]
                               ) -> Dict:
        """Deletes a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to delete
        :type team_user_group_id: str or int
        :return: Dict with team ID and `group_deleted` set to True
        """
        response = self.get_endpoint("team_user_groups"). \
            delete(parent_id=team_id, resource_id=team_user_group_id)
        return response

    def add_projects_to_group(self, team_id: Union[str, int],
                              team_user_group_id: Union[str, int],
                              params: Union[str, List[str]]
                              ) -> TeamUserGroupModel:
        """Adds projects to a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to add projects to
        :type team_user_group_id: str or int
        :param params: Project IDs to add to the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").add_projects(
            params=params,
            parent_id=team_id,
            resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def remove_projects_from_group(self, team_id: Union[str, int],
                                   team_user_group_id: Union[str, int],
                                   params: Union[str, List[str]]
                                   ) -> TeamUserGroupModel:
        """Removes projects from a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to remove projects from
        :type team_user_group_id: str or int
        :param params: Project IDs to remove from the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").remove_projects(
            params=params,
            parent_id=team_id,
            resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def add_members_to_group(self, team_id: Union[str, int],
                             team_user_group_id: Union[str, int],
                             params: Union[str, List[str]]
                             ) -> TeamUserGroupModel:
        """Adds members to a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to add members to
        :type team_user_group_id: str or int
        :param params: User IDs to add to the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").add_members(
            params=params,
            parent_id=team_id,
            resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def remove_members_from_group(self, team_id: Union[str, int],
                                  team_user_group_id: Union[str, int],
                                  params: Union[str, List[str]]
                                  ) -> TeamUserGroupModel:
        """Removes members from a team user group.

        :param team_id: ID of the team
        :type team_id: str or int
        :param team_user_group_id: ID of the team user group to remove members from
        :type team_user_group_id: str or int
        :param params: User IDs to remove from the group
        :type params: list or str
        :return: Team user group model
        """
        raw_group = self.get_endpoint("team_user_groups").remove_members(
            params=params,
            parent_id=team_id,
            resource_id=team_user_group_id
        )
        return TeamUserGroupModel(raw_group)

    def team_user_billing_details(
            self, team_id: str) -> TeamUsersBillingDetailsModel:
        """Fetches team user billing details.

        :param str team_id: ID of the team
        :return: Team users billing details model
        """
        raw_details = self.get_endpoint("team_user_billing_details"). \
            find(parent_id=team_id)
        return TeamUsersBillingDetailsModel(raw_details)

    def create_team_user_billing_details(self, team_id: str,
                                         params: Dict[str, str]
                                         ) -> TeamUsersBillingDetailsModel:
        """Creates team user billing details.

        :param str team_id: ID of the team
        :param dict params: Billing details parameters
        :return: Team users billing details model
        """
        raw_details = self.get_endpoint("team_user_billing_details"). \
            create(params=params, parent_id=team_id)
        return TeamUsersBillingDetailsModel(raw_details)

    def update_team_user_billing_details(self, team_id: str,
                                         params: Dict[str, str]
                                         ) -> TeamUsersBillingDetailsModel:
        """Updates team user billing details.

        :param str team_id: ID of the team
        :param dict params: Billing details parameters
        :return: Team users billing details model
        """
        raw_details = self.get_endpoint("team_user_billing_details"). \
            update(params=params, parent_id=team_id)
        return TeamUsersBillingDetailsModel(raw_details)

    def translations(self, project_id: str,
                     params: Optional[Dict] = None) -> TranslationsCollection:
        """Fetches all translations for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request parameters
        :return: Collection of translations
        """
        raw_translations = self.get_endpoint("translations"). \
            all(params=params, parent_id=project_id)
        return TranslationsCollection(raw_translations)

    def translation(self,
                    project_id: str,
                    translation_id: Union[str, int],
                    params: Optional[Dict] = None) -> TranslationModel:
        """Fetches a translation.

        :param str project_id: ID of the project
        :param translation_id: ID of the translation to fetch
        :type translation_id: int or str
        :param dict params: (optional) Request parameters
        :return: Task model
        """
        raw_translation = self.get_endpoint("translations"). \
            find(params, parent_id=project_id, resource_id=translation_id)
        return TranslationModel(raw_translation)

    def update_translation(self,
                           project_id: str,
                           translation_id: Union[str, int],
                           params: Dict[str, Any]) -> TranslationModel:
        """Updates a translation.

        :param str project_id: ID of the project
        :param translation_id: ID of the translation to update
        :type translation_id: int or str
        :param dict params: Translation parameters
        :return: Task model
        """
        raw_translation = self.get_endpoint("translations").update(
            params=params,
            parent_id=project_id,
            resource_id=translation_id
        )
        return TranslationModel(raw_translation)

    def translation_providers(self, team_id: Union[str, int],
                              params: Optional[Dict] = None
                              ) -> TranslationProvidersCollection:
        """Fetches all translation providers.

        :param team_id: ID of the team
        :type team_id: str or int
        :param dict params: (optional) Pagination parameters
        :return: Collection of translation providers
        """
        raw_providers = self.get_endpoint("translation_providers"). \
            all(params=params, parent_id=team_id)
        return TranslationProvidersCollection(raw_providers)

    def translation_provider(self, team_id: Union[str, int],
                             translation_provider_id: Union[str, int]
                             ) -> TranslationProviderModel:
        """Fetches a translation provider.

        :param team_id: ID of the team
        :type team_id: str or int
        :param translation_provider_id: ID of the translation provider to fetch
        :type translation_provider_id: str or int
        :return: Translation provider model
        """
        raw_provider = self.get_endpoint("translation_providers"). \
            find(parent_id=team_id, resource_id=translation_provider_id)
        return TranslationProviderModel(raw_provider)

    def translation_statuses(self, project_id: str,
                             params: Optional[Dict] = None
                             ) -> TranslationStatusesCollection:
        """Fetches all translation statuses.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination parameters
        :return: Collection of translation statuses
        """
        raw_statuses = self.get_endpoint("translation_statuses"). \
            all(params=params, parent_id=project_id)
        return TranslationStatusesCollection(raw_statuses)

    def translation_status(self, project_id: str,
                           translation_status_id: Union[str, int],
                           ) -> TranslationStatusModel:
        """Fetches a translation status.

        :param str project_id: ID of the project
        :param translation_status_id: ID of the status to fetch
        :type translation_status_id: int or str
        :return: Translation status model
        """
        raw_status = self.get_endpoint("translation_statuses"). \
            find(parent_id=project_id, resource_id=translation_status_id)
        return TranslationStatusModel(raw_status)

    def create_translation_status(self, project_id: str,
                                  params: Dict[str, str]
                                  ) -> TranslationStatusModel:
        """Creates a translation status.

        :param str project_id: ID of the project
        :param dict params: Translation status parameters
        :return: Translation status model
        """
        raw_status = self.get_endpoint("translation_statuses"). \
            create(params=params, parent_id=project_id)
        return TranslationStatusModel(raw_status)

    def update_translation_status(self, project_id: str,
                                  translation_status_id: Union[str, int],
                                  params: Optional[Dict[str, str]] = None
                                  ) -> TranslationStatusModel:
        """Updates a translation status.

        :param str project_id: ID of the project
        :param translation_status_id: ID of the status to update
        :type translation_status_id: int or str
        :param dict params: Translation status parameters
        :return: Translation status model
        """
        raw_status = self.get_endpoint("translation_statuses").update(
            params=params,
            parent_id=project_id,
            resource_id=translation_status_id
        )
        return TranslationStatusModel(raw_status)

    def delete_translation_status(self, project_id: str,
                                  translation_status_id: Union[str, int],
                                  ) -> Dict:
        """Deletes a translation status.

        :param str project_id: ID of the project
        :param translation_status_id: ID of the status to delete
        :type translation_status_id: int or str
        :return: Dict with project ID and `custom_translation_status_deleted`: True
        """
        response = self.get_endpoint("translation_statuses"). \
            delete(parent_id=project_id, resource_id=translation_status_id)
        return response

    def translation_statuses_colors(self, project_id: str) -> List:
        """Fetches available RGB colors that can be assigned to
        translation statuses.

        :param str project_id: ID of the project
        :return: List with the RGB color codes
        """
        response = self.get_endpoint("translation_statuses"). \
            colors(parent_id=project_id)
        return response["colors"]

    def webhooks(self, project_id: str,
                 params: Optional[Dict[str, str]] = None
                 ) -> WebhooksCollection:
        """Lists all webhooks set for a project.

        :param str project_id: ID of the project
        :param dict params: Pagination parameters
        :return: Webhook collection
        """
        raw_webhooks = self.get_endpoint("webhooks"). \
            all(params=params, parent_id=project_id)
        return WebhooksCollection(raw_webhooks)

    def webhook(self, project_id: str, webhook_id: str) -> WebhookModel:
        """Fetches a webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to fetch
        :return: Webhook model
        """
        raw_webhook = self.get_endpoint("webhooks"). \
            find(parent_id=project_id, resource_id=webhook_id)
        return WebhookModel(raw_webhook)

    def create_webhook(self, project_id: str,
                       params: Dict[str, str]
                       ) -> WebhookModel:
        """Creates a webhook.

        :param str project_id: ID of the project
        :param dict params: Webhook parameters
        :return: Webhook model
        """
        raw_webhook = self.get_endpoint("webhooks"). \
            create(params=params, parent_id=project_id)
        return WebhookModel(raw_webhook)

    def update_webhook(self, project_id: str, webhook_id: str,
                       params: Optional[Dict[str, str]] = None) -> WebhookModel:
        """Updates a webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to update
        :param dict params: Webhook parameters
        :return: Webhook model
        """
        raw_webhook = self.get_endpoint("webhooks"). \
            update(params=params, parent_id=project_id, resource_id=webhook_id)
        return WebhookModel(raw_webhook)

    def delete_webhook(self, project_id: str, webhook_id: str) -> Dict:
        """Deletes a webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to delete
        :return: Dict with project ID and `webhook_deleted` set to True
        """
        response = self.get_endpoint("webhooks"). \
            delete(parent_id=project_id, resource_id=webhook_id)
        return response

    def regenerate_webhook_secret(self, project_id: str,
                                  webhook_id: str) -> Dict:
        """Regenerates a secret key for the webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to regenerate secret for
        :return: Dict with project ID and `secret` with the new secret's value
        """
        response = self.get_endpoint("webhooks"). \
            regenerate_secret(parent_id=project_id, resource_id=webhook_id)
        return response
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
        camelized_name = snake_to_camel(endpoint_name)
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
