"""
lokalise.collections.base_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Collection parent class inherited by specific collections.
"""

from abc import ABC


class BaseCollection(ABC):
    """Abstract base class for resources collections.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    collection data. Response usually arrives in the following format:
    {"project_id": "abc", contributors: [{"user_id": 1}, {"user_id": 2}]}
    In this case, the DATA_KEY would be "contributors"

    :attribute MODEL_KLASS: tells which class to use to produce models for each
    item in the collection.
    """
    DATA_KEY = ''
    MODEL_KLASS = ''

    def __init__(self, raw_data):
        """Creates a new collection.
        To get access to collection data, use `items` attribute.
        Pagination-related data is stored inside the following attributes:

            total_count
            page_count
            limit
            current_page

        :param raw_data: Data returned by the API
        """
        self.project_id = raw_data.get('project_id', None)
        self.branch = raw_data.get('branch', None)
        self.errors = raw_data.get('errors', None)
        raw_items = raw_data[self.DATA_KEY]
        self.items = []
        for item in raw_items:
            self.items.append(self.MODEL_KLASS(item))  # pylint: disable=E1102

        pagination = raw_data.get("_pagination", {})
        if pagination:
            self.total_count = int(pagination.get(
                "x-pagination-total-count", 0))
            self.page_count = int(pagination.get("x-pagination-page-count", 0))
            self.limit = int(pagination.get("x-pagination-limit", 0))
            self.current_page = int(pagination.get("x-pagination-page", 0))

    def is_last_page(self):
        """Checks whether the current collection set is the last page.

        :rtype: boolean
        """
        return not self.has_next_page()

    def is_first_page(self):
        """Checks whether the current collection set is the first page.

        :rtype: boolean
        """
        return not self.has_prev_page()

    def has_next_page(self):
        """Checks whether the current collection set has the next page.

        :rtype: boolean
        """
        return self.current_page > 0 and self.current_page < self.page_count

    def has_prev_page(self):
        """Checks whether the current collection set has the previous page.

        :rtype: boolean
        """
        return self.current_page > 1
