from typing import Any, ClassVar, TypeVar

from lokalise.collections.base_collection import BaseCollection
from lokalise.mixins.cursor_pagination import CursorPaginationMixin
from lokalise.models.base_model import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)


class BaseCollectionV1(CursorPaginationMixin, BaseCollection[TModel]):
    DATA_KEY: ClassVar[str]

    def __init__(self, raw_data: dict[str, Any]) -> None: ...