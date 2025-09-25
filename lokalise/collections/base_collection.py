"""
lokalise.collections.base_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Collection parent class inherited by specific collections.
"""

from typing import Any, Generic, TypeVar, cast, ClassVar

from ..models.base_model import BaseModel


TModel = TypeVar("TModel", bound=BaseModel)


class BaseCollection(Generic[TModel]):
    """Abstract base class for resources collections.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    collection data. Response usually arrives in the following format:
    {"project_id": "abc", contributors: [{"user_id": 1}, {"user_id": 2}]}
    In this case, the DATA_KEY would be "contributors"

    :attribute MODEL_KLASS: tells which class to use to produce models for each
    item in the collection.

    :attribute COMMON_ATTRS: list of common attributes that the collections may have.
    """

    DATA_KEY: str = ""
    MODEL_KLASS: ClassVar[type[BaseModel]] = BaseModel
    COMMON_ATTRS: ClassVar[list[str]] = ["project_id", "user_id", "branch", "errors", "team_id"]

    items: list[TModel]
    total_count: int
    page_count: int
    limit: int
    current_page: int
    next_cursor: str | None

    project_id: str | None = None
    user_id: int | None = None
    branch: str | None = None
    errors: Any | None = None
    team_id: int | None = None

    def __init__(self, raw_data: dict[str, Any]) -> None:
        """Creates a new collection.
        To get access to collection data, use `items` attribute.
        Pagination-related data is stored inside the following attributes:

            total_count
            page_count
            limit
            current_page

        :param raw_data: Data returned by the API
        """
        self.__extract_common_attrs(raw_data)

        raw_items_any = raw_data.get(self.DATA_KEY, [])
        if not isinstance(raw_items_any, list):
            raw_items_any = []
        raw_items = cast(list[dict[str, Any]], raw_items_any)

        model_klass = cast(type[TModel], self.MODEL_KLASS)

        self.items = []
        for item in raw_items:
            self.items.append(model_klass(item))

        pagination = cast(dict[str, Any], raw_data.get("_pagination", {}))
        if pagination:
            self.total_count = int(pagination.get("x-pagination-total-count", 0) or 0)
            self.page_count = int(pagination.get("x-pagination-page-count", 0) or 0)
            self.limit = int(pagination.get("x-pagination-limit", 0) or 0)
            self.current_page = int(pagination.get("x-pagination-page", 0) or 0)
            self.next_cursor = cast(str | None, pagination.get("x-pagination-next-cursor", None))

    def is_last_page(self) -> bool:
        """Checks whether the current collection set is the last page.

        :rtype: bool
        """
        return not self.has_next_page()

    def is_first_page(self) -> bool:
        """Checks whether the current collection set is the first page.

        :rtype: bool
        """
        return not self.has_prev_page()

    def has_next_page(self) -> bool:
        """Checks whether the current collection set has the next page.

        :rtype: bool
        """
        return self.current_page > 0 and self.current_page < self.page_count

    def has_prev_page(self) -> bool:
        """Checks whether the current collection set has the previous page.

        :rtype: bool
        """
        return self.current_page > 1

    def has_next_cursor(self) -> bool:
        """Checks whether the current collection set has the next cursor.

        :rtype: bool
        """
        return self.next_cursor is not None

    def __extract_common_attrs(self, raw_data: dict[str, Any]) -> None:
        """Fetches common data from the response and sets the
        corresponding attributes.
        """
        for attr in self.COMMON_ATTRS:
            if attr in raw_data:
                setattr(self, attr, raw_data[attr])
