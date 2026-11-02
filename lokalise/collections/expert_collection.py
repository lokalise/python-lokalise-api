
"""
lokalise.collections.expert_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Base collection for Lokalise Expert API resources.
"""

from typing import Any, ClassVar

from .base_collection import BaseCollection, TModel
from ..response import ApiResponse
from ..mixins.expert_pagination import ExpertPaginationMixin


class ExpertCollection(ExpertPaginationMixin, BaseCollection[TModel]):
    """Collection with Expert API pagination metadata."""

    COMMON_ATTRS: ClassVar[tuple[str, ...]] = (
        "project_id",
        "user_id",
        "branch",
        "errors",
        "team_id",
    )

    project_id: str | None = None
    user_id: int | None = None
    branch: str | None = None
    errors: Any = None
    team_id: int | None = None

    def __init__(self, response: ApiResponse) -> None:
        super().__init__(response)
        self._load_pagination(response)
