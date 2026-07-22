"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""

from .base_client import BaseClient
from .client_methods.branches import BranchMethods
from .client_methods.comments import CommentMethods
from .client_methods.contributors import ContributorMethods
from .client_methods.files import FileMethods
from .client_methods.glossary_terms import GlossaryTermsMethods
from .client_methods.jwt import JwtMethods
from .client_methods.keys import KeyMethods
from .client_methods.languages import LanguageMethods
from .client_methods.orders import OrderMethods
from .client_methods.payment_cards import PaymentCardMethods
from .client_methods.permission_templates import PermissionTemplateMethods
from .client_methods.processes import ProcessMethods
from .client_methods.projects import ProjectMethods
from .client_methods.screenshots import ScreenshotMethods
from .client_methods.segments import SegmentMethods
from .client_methods.snapshots import SnapshotMethods
from .client_methods.tasks import TaskMethods
from .client_methods.team_user_billing_details import TeamUserBillingDetailsMethods
from .client_methods.team_user_groups import TeamUserGroupMethods
from .client_methods.team_users import TeamUserMethods
from .client_methods.teams import TeamMethods
from .client_methods.translation_providers import TranslationProviderMethods
from .client_methods.translation_statuses import TranslationStatusMethods
from .client_methods.translations import TranslationMethods
from .client_methods.webhooks import WebhookMethods


class Client(
    BaseClient,
    BranchMethods,
    CommentMethods,
    ContributorMethods,
    FileMethods,
    GlossaryTermsMethods,
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
    WebhookMethods,
):
    """Client used to send API requests.

    Usage:

        import lokalise
        client = lokalise.Client('api_token')
        client.projects()
    """
