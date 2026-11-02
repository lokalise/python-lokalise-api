
"""
Tests for Expert API collections and pagination.
"""

from typing import Any, cast
from unittest.mock import Mock, patch

import pytest
from requests import Response

from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.base_model import BaseModel
from lokalise.response import ApiResponse


class DummyExpertCollection(ExpertCollection[BaseModel]):
    DATA_KEY = "items"


def _response(
    data: dict[str, Any] | None = None,
    *,
    headers: dict[str, str] | None = None,
) -> ApiResponse:
    """Create an API response with mocked HTTP data."""
    raw = Mock(spec=Response)
    raw.json.return_value = data if data is not None else {"items": []}
    raw.status_code = 200
    raw.headers = headers or {}

    with patch("lokalise.response.raise_on_error"):
        return ApiResponse(cast(Response, raw))


def test_defaults_pagination_values_when_missing() -> None:
    collection = DummyExpertCollection(_response())

    assert collection.total_count == 0
    assert collection.page_count == 0
    assert collection.limit == 0
    assert collection.current_page == 0
    assert collection.next_cursor is None


def test_extracts_pagination_from_headers() -> None:
    response = _response(
        headers={
            "X-Pagination-Total-Count": "42",
            "X-Pagination-Page-Count": "5",
            "X-Pagination-Limit": "10",
            "X-Pagination-Page": "2",
            "X-Pagination-Next-Cursor": "next-page",
        },
    )

    collection = DummyExpertCollection(response)

    assert collection.total_count == 42
    assert collection.page_count == 5
    assert collection.limit == 10
    assert collection.current_page == 2
    assert collection.next_cursor == "next-page"


def test_extracts_common_attributes() -> None:
    collection = DummyExpertCollection(
        _response({
            "items": [],
            "project_id": "project-id",
            "user_id": 123,
            "branch": "main",
            "errors": ["something"],
            "team_id": 456,
        })
    )

    assert collection.project_id == "project-id"
    assert collection.user_id == 123
    assert collection.branch == "main"
    assert collection.errors == ["something"]
    assert collection.team_id == 456


def test_common_attributes_default_to_none() -> None:
    collection = DummyExpertCollection(_response())

    assert collection.project_id is None
    assert collection.user_id is None
    assert collection.branch is None
    assert collection.errors is None
    assert collection.team_id is None


@pytest.mark.parametrize(
    ("page", "has_next", "has_prev", "is_first", "is_last"),
    [
        (1, True, False, True, False),
        (2, True, True, False, False),
        (3, False, True, False, True),
    ],
)
def test_page_helpers(
    page: int,
    has_next: bool,
    has_prev: bool,
    is_first: bool,
    is_last: bool,
) -> None:
    collection = DummyExpertCollection(
        _response(
            headers={
                "X-Pagination-Page-Count": "3",
                "X-Pagination-Page": str(page),
            }
        )
    )

    assert collection.has_next_page() is has_next
    assert collection.has_prev_page() is has_prev
    assert collection.is_first_page() is is_first
    assert collection.is_last_page() is is_last


def test_has_next_cursor() -> None:
    collection = DummyExpertCollection(
        _response(
            headers={
                "X-Pagination-Next-Cursor": "cursor",
            }
        )
    )

    assert collection.has_next_cursor()


def test_has_no_next_cursor_by_default() -> None:
    collection = DummyExpertCollection(_response())

    assert not collection.has_next_cursor()


def test_does_not_inject_pagination_into_json() -> None:
    response = _response(
        headers={
            "X-Pagination-Page": "2",
        }
    )

    collection = DummyExpertCollection(response)

    assert collection.current_page == 2
    assert "_pagination" not in response


def test_rejects_invalid_pagination_header() -> None:
    response = _response(
        headers={
            "X-Pagination-Page": "invalid",
        }
    )

    with pytest.raises(ValueError):
        DummyExpertCollection(response)
