
"""
lokalise.collections.v1.base_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Base collection for Lokalise API v1 resources.
"""

from typing import Any, ClassVar

from lokalise.collections.base_collection import BaseCollection, TModel
from lokalise.mixins.cursor_pagination import CursorPaginationMixin


class BaseCollectionV1(CursorPaginationMixin, BaseCollection[TModel]):
    """Collection for API v1 cursor-paginated responses."""

    DATA_KEY: ClassVar[str] = "data"

    def __init__(self, raw_data: dict[str, Any]) -> None:
        super().__init__(raw_data)

        self._set_cursor_pagination(
            has_more=raw_data.get("has_more", False),
            next_cursor=raw_data.get("next_cursor"),
        )
