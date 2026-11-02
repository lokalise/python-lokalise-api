from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, TypeVar, overload

from lokalise.models.base_model import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)


class BaseCollection(Sequence[TModel]):
    DATA_KEY: ClassVar[str]
    COMMON_ATTRS: ClassVar[tuple[str, ...]]
    MODEL_KLASS: ClassVar[type[BaseModel]]

    items: list[TModel]

    def __init__(self, raw_data: dict[str, Any]) -> None: ...
    def __iter__(self) -> Iterator[TModel]: ...
    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> TModel: ...
    @overload
    def __getitem__(self, index: slice) -> list[TModel]: ...