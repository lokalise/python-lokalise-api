import pytest
from lokalise.collections.base_collection import BaseCollection
from lokalise.models.base_model import BaseModel


class DummyCollection(BaseCollection[BaseModel]):
    DATA_KEY = "items"


def test_rejects_non_list_collection_data() -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'items' to be a list, got dict",
    ):
        DummyCollection({"items": {"id": 1}})


@pytest.mark.parametrize(
    "items",
    [
        ["invalid"],
        [123],
        [None],
        [{"id": 1}, "invalid"],
    ],
)
def test_rejects_non_dictionary_collection_items(
    items: list[object],
) -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'items' items to be dictionaries",
    ):
        DummyCollection({"items": items})


def test_rejects_non_dictionary_pagination() -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected '_pagination' to be a dictionary",
    ):
        DummyCollection(
            {
                "items": [],
                "_pagination": "invalid",
            }
        )


def test_defaults_to_empty_collection() -> None:
    collection = DummyCollection({})

    assert collection.items == []


def test_defaults_pagination_values_when_missing() -> None:
    collection = DummyCollection({"items": []})

    assert collection.total_count == 0
    assert collection.page_count == 0
    assert collection.limit == 0
    assert collection.current_page == 0
    assert collection.next_cursor is None


def test_extracts_pagination_values() -> None:
    collection = DummyCollection(
        {
            "items": [],
            "_pagination": {
                "x-pagination-total-count": "42",
                "x-pagination-page-count": "5",
                "x-pagination-limit": "10",
                "x-pagination-page": "2",
                "x-pagination-next-cursor": "next-page",
            },
        }
    )

    assert collection.total_count == 42
    assert collection.page_count == 5
    assert collection.limit == 10
    assert collection.current_page == 2
    assert collection.next_cursor == "next-page"


def test_extracts_common_attributes() -> None:
    collection = DummyCollection(
        {
            "items": [],
            "project_id": "project-id",
            "user_id": 123,
            "branch": "main",
            "errors": ["something"],
            "team_id": 456,
        }
    )

    assert collection.project_id == "project-id"
    assert collection.user_id == 123
    assert collection.branch == "main"
    assert collection.errors == ["something"]
    assert collection.team_id == 456


def test_common_attributes_default_to_none() -> None:
    collection = DummyCollection({"items": []})

    assert collection.project_id is None
    assert collection.user_id is None
    assert collection.branch is None
    assert collection.errors is None
    assert collection.team_id is None


def test_page_helpers() -> None:
    collection = DummyCollection(
        {
            "items": [],
            "_pagination": {
                "x-pagination-page-count": "3",
                "x-pagination-page": "2",
            },
        }
    )

    assert collection.has_next_page()
    assert collection.has_prev_page()
    assert not collection.is_first_page()
    assert not collection.is_last_page()


def test_first_page_helpers() -> None:
    collection = DummyCollection(
        {
            "items": [],
            "_pagination": {
                "x-pagination-page-count": "3",
                "x-pagination-page": "1",
            },
        }
    )

    assert collection.has_next_page()
    assert not collection.has_prev_page()
    assert collection.is_first_page()
    assert not collection.is_last_page()


def test_last_page_helpers() -> None:
    collection = DummyCollection(
        {
            "items": [],
            "_pagination": {
                "x-pagination-page-count": "3",
                "x-pagination-page": "3",
            },
        }
    )

    assert not collection.has_next_page()
    assert collection.has_prev_page()
    assert not collection.is_first_page()
    assert collection.is_last_page()


def test_has_next_cursor() -> None:
    collection = DummyCollection(
        {
            "items": [],
            "_pagination": {
                "x-pagination-next-cursor": "cursor",
            },
        }
    )

    assert collection.has_next_cursor()


def test_has_no_next_cursor_by_default() -> None:
    collection = DummyCollection({"items": []})

    assert not collection.has_next_cursor()
