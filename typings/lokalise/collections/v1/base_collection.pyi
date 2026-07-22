from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, Generic, TypeVar, overload

from lokalise.models.base_model import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)

class BaseCollectionV1(Sequence[TModel], Generic[TModel]):
    DATA_KEY: ClassVar[str]
    MODEL_KLASS: ClassVar[type[BaseModel]]

    items: list[TModel]
    has_more: bool
    next_cursor: str | None

    def __init__(self, raw_data: dict[str, Any]) -> None: ...
    def __iter__(self) -> Iterator[TModel]: ...
    @overload
    def __getitem__(self, index: int) -> TModel: ...
    @overload
    def __getitem__(self, index: slice) -> list[TModel]: ...
    def __len__(self) -> int: ...
    def has_next_cursor(self) -> bool: ...
    def is_last_page(self) -> bool: ...
