from typing import Any, ClassVar

from .base_collection import BaseCollection, TModel
from lokalise.mixins.cursor_pagination import CursorPaginationMixin


class VantageCollection(CursorPaginationMixin, BaseCollection[TModel]):
    DATA_KEY: ClassVar[str]

    meta_count: int

    def __init__(self, raw_data: dict[str, Any]) -> None: ...

    @property
    def cursor(self) -> str | None: ...