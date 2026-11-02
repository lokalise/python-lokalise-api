from typing import Any, ClassVar

from lokalise.response import ApiResponse

from .base_collection import BaseCollection, TModel
from lokalise.mixins.expert_pagination import ExpertPaginationMixin


class ExpertCollection(ExpertPaginationMixin, BaseCollection[TModel]):
    COMMON_ATTRS: ClassVar[tuple[str, ...]]

    project_id: str | None
    user_id: int | None
    branch: str | None
    errors: Any
    team_id: int | None

    def __init__(self, response: ApiResponse) -> None: ...