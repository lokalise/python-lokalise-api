
"""
lokalise.mixins.cursor_pagination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cursor pagination behavior for collections.
"""


class CursorPaginationMixin:
    """Shared behavior for cursor-paginated collections."""

    has_more: bool
    next_cursor: str | None

    def _set_cursor_pagination(
        self,
        *,
        has_more: object,
        next_cursor: object,
    ) -> None:
        if not isinstance(has_more, bool):
            raise TypeError("Expected 'has_more' to be a boolean")

        if next_cursor is not None and not isinstance(next_cursor, str):
            raise TypeError("Expected 'next_cursor' to be a string or None")

        if has_more and not next_cursor:
            raise ValueError(
                "'next_cursor' must be provided when 'has_more' is true"
            )

        self.has_more = has_more
        self.next_cursor = next_cursor

    def has_next_cursor(self) -> bool:
        """Return whether a next cursor is available."""
        return self.has_more and self.next_cursor is not None

    def has_next_page(self) -> bool:
        """Return whether more results are available."""
        return self.has_more

    def is_last_page(self) -> bool:
        """Return whether this is the final result set."""
        return not self.has_more
