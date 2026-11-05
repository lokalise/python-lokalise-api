"""
lokalise.client_methods.endpoint_provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A simple mixin with a shared protocol.
"""

from typing import TYPE_CHECKING, Literal, Protocol, overload

from lokalise.endpoints.base_endpoint import BaseEndpoint

if TYPE_CHECKING:
    from lokalise.endpoints.branches_endpoint import BranchesEndpoint
    from lokalise.endpoints.files_endpoint import FilesEndpoint
    from lokalise.endpoints.projects_endpoint import ProjectsEndpoint
    from lokalise.endpoints.team_user_groups_endpoint import TeamUserGroupsEndpoint
    from lokalise.endpoints.translation_statuses_endpoint import TranslationStatusesEndpoint
    from lokalise.endpoints.webhooks_endpoint import WebhooksEndpoint

class EndpointProviderMixin(Protocol):
    """Protocol for classes that provide endpoint loading."""

    def get_endpoint(
        self,
        name: str,
        namespace: str | None = None,
    ) -> BaseEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: Literal["branches"],
    ) -> BranchesEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: Literal["files"],
    ) -> FilesEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: Literal["webhooks"],
    ) -> WebhooksEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: Literal["translation_statuses"],
    ) -> TranslationStatusesEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: Literal["team_user_groups"],
    ) -> TeamUserGroupsEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: Literal["projects"],
    ) -> ProjectsEndpoint: ...

    @overload
    def expert_endpoint(
        self,
        name: str,
    ) -> BaseEndpoint:
        ...

    def expert_endpoint(self, name: str) -> BaseEndpoint:
        """Load an Expert API endpoint with specialized typing."""
        return self.get_endpoint(name)