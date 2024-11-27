"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""
from typing import Any, Callable
import importlib
from lokalise.utils import snake_to_camel
from .base_client import BaseClient
from .client_methods.branches import BranchMethods
from .client_methods.comments import CommentMethods
from .client_methods.contributors import ContributorMethods
from .client_methods.files import FileMethods
from .client_methods.jwt import JwtMethods
from .client_methods.keys import KeyMethods
from .client_methods.languages import LanguageMethods
from .client_methods.orders import OrderMethods
from .client_methods.payment_cards import PaymentCardMethods
from .client_methods.permission_templates import PermissionTemplateMethods
from .client_methods.projects import ProjectMethods
from .client_methods.processes import ProcessMethods
from .client_methods.snapshots import SnapshotMethods
from .client_methods.screenshots import ScreenshotMethods
from .client_methods.segments import SegmentMethods
from .client_methods.tasks import TaskMethods
from .client_methods.teams import TeamMethods
from .client_methods.team_users import TeamUserMethods
from .client_methods.team_user_groups import TeamUserGroupMethods
from .client_methods.team_user_billing_details import TeamUserBillingDetailsMethods
from .client_methods.translations import TranslationMethods
from .client_methods.translation_providers import TranslationProviderMethods
from .client_methods.translation_statuses import TranslationStatusMethods
from .client_methods.webhooks import WebhookMethods


class Client(
        BaseClient,
        BranchMethods,
        CommentMethods,
        ContributorMethods,
        FileMethods,
        JwtMethods,
        KeyMethods,
        LanguageMethods,
        OrderMethods,
        PaymentCardMethods,
        PermissionTemplateMethods,
        ProjectMethods,
        ProcessMethods,
        SnapshotMethods,
        ScreenshotMethods,
        SegmentMethods,
        TaskMethods,
        TeamMethods,
        TeamUserMethods,
        TeamUserGroupMethods,
        TeamUserBillingDetailsMethods,
        TranslationMethods,
        TranslationProviderMethods,
        TranslationStatusMethods,
        WebhookMethods):
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
