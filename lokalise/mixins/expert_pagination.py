
"""
lokalise.collections.expert_pagination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pagination behavior for Lokalise Expert collections.
"""

from lokalise.response import ApiResponse

class ExpertPaginationMixin:
    """Pagination metadata from Lokalise Expert API headers."""

    total_count: int
    page_count: int
    limit: int
    current_page: int
    next_cursor: str | None

    def _load_pagination(self, response: ApiResponse) -> None:
        headers = response.headers

        self.total_count = int(
            headers.get("x-pagination-total-count", 0) or 0
        )
        self.page_count = int(
            headers.get("x-pagination-page-count", 0) or 0
        )
        self.limit = int(
            headers.get("x-pagination-limit", 0) or 0
        )
        self.current_page = int(
            headers.get("x-pagination-page", 0) or 0
        )
        self.next_cursor = headers.get("x-pagination-next-cursor")

    def is_last_page(self) -> bool:
        return not self.has_next_page()

    def is_first_page(self) -> bool:
        return not self.has_prev_page()

    def has_next_page(self) -> bool:
        return 0 < self.current_page < self.page_count

    def has_prev_page(self) -> bool:
        return self.current_page > 1

    def has_next_cursor(self) -> bool:
        return self.next_cursor is not None