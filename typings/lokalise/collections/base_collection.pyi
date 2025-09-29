from collections.abc import Sequence
from typing import Any, ClassVar, Generic, TypeVar, overload

from lokalise.models.base_model import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)

class BaseCollection(Sequence[TModel], Generic[TModel]):
    DATA_KEY: ClassVar[str]
    COMMON_ATTRS: ClassVar[list[str]]

    MODEL_KLASS: ClassVar[type[BaseModel]]

    items: list[TModel]

    total_count: int
    page_count: int
    limit: int
    current_page: int
    next_cursor: str | None

    project_id: str | None
    user_id: int | None
    branch: str | None
    errors: Any | None
    team_id: int | None

    def __init__(self, raw_data: dict[str, Any]) -> None: ...
    @overload
    def __getitem__(self, index: int) -> TModel: ...
    @overload
    def __getitem__(self, index: slice) -> list[TModel]: ...
    def __len__(self) -> int: ...
    def is_last_page(self) -> bool: ...
    def is_first_page(self) -> bool: ...
    def has_next_page(self) -> bool: ...
    def has_prev_page(self) -> bool: ...
    def has_next_cursor(self) -> bool: ...
