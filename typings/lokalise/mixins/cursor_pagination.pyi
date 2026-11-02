class CursorPaginationMixin:
    has_more: bool
    next_cursor: str | None

    def _set_cursor_pagination(
        self,
        *,
        has_more: object,
        next_cursor: object,
    ) -> None: ...

    def has_next_cursor(self) -> bool: ...
    def has_next_page(self) -> bool: ...
    def is_last_page(self) -> bool: ...