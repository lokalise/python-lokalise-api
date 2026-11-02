
"""
Tests for API v1 collections and cursor pagination.
"""

import pytest

from lokalise.collections.v1.base_collection import BaseCollectionV1
from lokalise.models.base_model import BaseModel


class DummyCollection(BaseCollectionV1[BaseModel]):
    pass


def test_defaults_to_empty_collection() -> None:
    collection = DummyCollection({})

    assert collection.items == []
    assert len(collection) == 0
    assert collection.has_more is False
    assert collection.next_cursor is None
    assert not collection.has_next_page()
    assert not collection.has_next_cursor()
    assert collection.is_last_page()


def test_rejects_non_list_collection_data() -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'data' to be a list, got dict",
    ):
        DummyCollection({"data": {"id": 1}})


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
        match="Expected 'has_more' to be a boolean",
    ):
        DummyCollection({
            "data": [],
            "has_more": has_more,
        })


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
        match="Expected 'next_cursor' to be a string or None",
    ):
        DummyCollection({
            "data": [],
            "next_cursor": next_cursor,
        })


@pytest.mark.parametrize("next_cursor", [None, ""])
def test_requires_cursor_when_has_more_is_true(
    next_cursor: str | None,
) -> None:
    with pytest.raises(
        ValueError,
        match="'next_cursor' must be provided when 'has_more' is true",
    ):
        DummyCollection({
            "data": [],
            "has_more": True,
            "next_cursor": next_cursor,
        })


def test_accepts_cursor_when_has_more_is_true() -> None:
    collection = DummyCollection({
        "data": [],
        "has_more": True,
        "next_cursor": "next-page",
    })

    assert collection.has_more is True
    assert collection.next_cursor == "next-page"
    assert collection.has_next_cursor()
    assert collection.has_next_page()
    assert not collection.is_last_page()


@pytest.mark.parametrize("next_cursor", [None, "", "last-page"])
def test_final_page(
    next_cursor: str | None,
) -> None:
    collection = DummyCollection({
        "data": [],
        "has_more": False,
        "next_cursor": next_cursor,
    })

    assert collection.has_more is False
    assert collection.next_cursor == next_cursor
    assert not collection.has_next_cursor()
    assert not collection.has_next_page()
    assert collection.is_last_page()
