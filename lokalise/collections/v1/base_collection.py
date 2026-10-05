"""
lokalise.collections.v1.base_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Collection parent class inherited by specific collections (for the new v1 endpoint only).
"""

from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, TypeVar, cast, overload

from lokalise.models.base_model import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)


class BaseCollectionV1(Sequence[TModel]):
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

    DATA_KEY: ClassVar[str] = "data"
    MODEL_KLASS: ClassVar[type[BaseModel]] = BaseModel

    items: list[TModel]
    has_more: bool
    next_cursor: str | None

    def __init__(self, raw_data: dict[str, Any]) -> None:
        """Create a collection from an API v1 response.

        Args:
            raw_data: Data returned by the API.
        """
        self.items = self.__build_items(raw_data)
        self.__extract_pagination(raw_data)

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

    def __build_items(self, raw_data: dict[str, Any]) -> list[TModel]:
        raw_items_value = raw_data.get(self.DATA_KEY, [])

        if not isinstance(raw_items_value, list):
            raise TypeError(
                f"Expected '{self.DATA_KEY}' to be a list, " f"got {type(raw_items_value).__name__}"
            )

        raw_items_objects = cast(list[object], raw_items_value)

        if not all(isinstance(item, dict) for item in raw_items_objects):
            raise TypeError(f"Expected '{self.DATA_KEY}' items to be dictionaries")

        raw_items = cast(list[dict[str, Any]], raw_items_objects)
        model_klass = cast(type[TModel], self.MODEL_KLASS)

        return [model_klass(item) for item in raw_items]

    def __extract_pagination(self, raw_data: dict[str, Any]) -> None:
        has_more = raw_data.get("has_more", False)

        if not isinstance(has_more, bool):
            raise TypeError("Expected 'has_more' to be a boolean")

        next_cursor = raw_data.get("next_cursor")

        if next_cursor is not None and not isinstance(next_cursor, str):
            raise TypeError("Expected 'next_cursor' to be a string or None")

        if has_more and not next_cursor:
            raise ValueError("'next_cursor' must be provided when 'has_more' is true")

        self.has_more = has_more
        self.next_cursor = next_cursor
