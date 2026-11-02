
"""
lokalise.collections.vantage_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Base collection for Lokalise Vantage API resources.
"""

from typing import Any, ClassVar, cast

from .base_collection import BaseCollection, TModel
from lokalise.mixins.cursor_pagination import CursorPaginationMixin


class VantageCollection(CursorPaginationMixin, BaseCollection[TModel]):
    """Collection for Vantage API cursor-paginated responses."""

    DATA_KEY: ClassVar[str] = "data"

    meta_count: int

    def __init__(self, raw_data: dict[str, Any]) -> None:
        super().__init__(raw_data)
        self._load_pagination(raw_data)

    @property
    def cursor(self) -> str | None:
        """Return the cursor from Vantage pagination metadata."""
        return self.next_cursor

    def _load_pagination(self, raw_data: dict[str, Any]) -> None:
        raw_meta: object = raw_data.get("meta")

        if not isinstance(raw_meta, dict):
            raise ValueError("Vantage pagination metadata is missing")

        meta = cast(dict[str, object], raw_meta)

        try:
            count = meta["count"]
            has_more = meta["hasMore"]
        except KeyError as exc:
            raise ValueError(
                f"Missing Vantage pagination field: {exc.args[0]}"
            ) from exc

        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            raise TypeError(
                "Expected 'meta.count' to be a non-negative integer"
            )

        self._set_cursor_pagination(
            has_more=has_more,
            next_cursor=meta.get("cursor"),
        )

        self.meta_count = count
