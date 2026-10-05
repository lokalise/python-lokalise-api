import pytest
from lokalise.collections.v1.base_collection import BaseCollectionV1
from lokalise.models.base_model import BaseModel


class DummyCollection(BaseCollectionV1[BaseModel]):
    pass


def test_defaults_to_empty_collection() -> None:
    collection = DummyCollection({})

    assert collection.items == []


def test_rejects_non_list_collection_data() -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'data' to be a list, got dict",
    ):
        DummyCollection({"data": {"id": 1}})


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
        match=r"Expected 'data' items to be dictionaries",
    ):
        DummyCollection({"data": items})


def test_defaults_pagination_values() -> None:
    collection = DummyCollection({"data": []})

    assert collection.has_more is False
    assert collection.next_cursor is None


@pytest.mark.parametrize(
    "has_more",
    [
        "true",
        "false",
        1,
        0,
        None,
        [],
        {},
    ],
)
def test_rejects_non_boolean_has_more(
    has_more: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'has_more' to be a boolean",
    ):
        DummyCollection(
            {
                "data": [],
                "has_more": has_more,
            }
        )


@pytest.mark.parametrize(
    "next_cursor",
    [
        123,
        True,
        [],
        {},
    ],
)
def test_rejects_invalid_next_cursor(
    next_cursor: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'next_cursor' to be a string or None",
    ):
        DummyCollection(
            {
                "data": [],
                "next_cursor": next_cursor,
            }
        )


def test_requires_cursor_when_has_more_is_true() -> None:
    with pytest.raises(
        ValueError,
        match=r"'next_cursor' must be provided when 'has_more' is true",
    ):
        DummyCollection(
            {
                "data": [],
                "has_more": True,
            }
        )


def test_rejects_empty_cursor_when_has_more_is_true() -> None:
    with pytest.raises(
        ValueError,
        match=r"'next_cursor' must be provided when 'has_more' is true",
    ):
        DummyCollection(
            {
                "data": [],
                "has_more": True,
                "next_cursor": "",
            }
        )


def test_accepts_cursor_when_has_more_is_true() -> None:
    collection = DummyCollection(
        {
            "data": [],
            "has_more": True,
            "next_cursor": "next-page",
        }
    )

    assert collection.has_more is True
    assert collection.next_cursor == "next-page"
    assert collection.has_next_cursor()
    assert not collection.is_last_page()


def test_final_page_has_no_next_cursor() -> None:
    collection = DummyCollection(
        {
            "data": [],
            "has_more": False,
            "next_cursor": None,
        }
    )

    assert not collection.has_next_cursor()
    assert collection.is_last_page()
