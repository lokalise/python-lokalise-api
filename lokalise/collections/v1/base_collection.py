"""
lokalise.collections.v1.base_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Collection parent class inherited by specific collections (for the new v1 endpoint only).
"""

from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, Generic, TypeVar, cast, overload

from lokalise.models.base_model import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)


class BaseCollectionV1(Sequence[TModel], Generic[TModel]):
    """Base collection for API v1 cursor-paginated responses.

    API responses are expected to have the following structure:

        {
            "data": [...],
            "has_more": true,
            "next_cursor": "eyJpZ..."
        }

    ``MODEL_KLASS`` specifies which model class should be used for
    individual items.
    """

    DATA_KEY: str = "data"
    MODEL_KLASS: ClassVar[type[BaseModel]] = BaseModel

    items: list[TModel]
    has_more: bool
    next_cursor: str | None

    def __init__(self, raw_data: dict[str, Any]) -> None:
        """Create a collection from an API v1 response.

        Args:
            raw_data: Data returned by the API.
        """
        raw_items_value = raw_data.get(self.DATA_KEY, [])

        if not isinstance(raw_items_value, list):
            raw_items_value = []  # pragma: no cover

        raw_items = [
            cast(dict[str, Any], item)
            for item in cast(list[object], raw_items_value)
            if isinstance(item, dict)
        ]

        model_klass = cast(type[TModel], self.MODEL_KLASS)
        self.items = [model_klass(item) for item in raw_items]

        has_more = raw_data.get("has_more", False)
        self.has_more = has_more if isinstance(has_more, bool) else False

        next_cursor = raw_data.get("next_cursor")
        self.next_cursor = next_cursor if isinstance(next_cursor, str) else None

    def __iter__(self) -> Iterator[TModel]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    @overload
    def __getitem__(self, index: int) -> TModel: ...

    @overload
    def __getitem__(self, index: slice) -> list[TModel]: ...

    def __getitem__(self, index: int | slice) -> TModel | list[TModel]:
        return self.items[index]

    def has_next_cursor(self) -> bool:
        """Return whether another cursor is available."""
        return self.has_more and self.next_cursor is not None

    def is_last_page(self) -> bool:
        """Return whether this is the final result set."""
        return not self.has_more
