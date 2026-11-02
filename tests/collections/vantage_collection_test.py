
"""
Tests for Vantage API collections and cursor pagination.
"""

import pytest

from lokalise.collections.vantage_collection import VantageCollection
from lokalise.models.base_model import BaseModel


class DummyVantageCollection(VantageCollection[BaseModel]):
    pass


def test_extracts_pagination_metadata() -> None:
    collection = DummyVantageCollection({
        "data": [],
        "meta": {
            "count": 10,
            "cursor": "next123",
            "hasMore": True,
        },
    })

    assert collection.meta_count == 10
    assert collection.cursor == "next123"
    assert collection.next_cursor == "next123"
    assert collection.has_more is True

    assert collection.has_next_page()
    assert collection.has_next_cursor()
    assert not collection.is_last_page()


def test_last_page_with_cursor() -> None:
    collection = DummyVantageCollection({
        "data": [],
        "meta": {
            "count": 5,
            "cursor": "last123",
            "hasMore": False,
        },
    })

    assert collection.cursor == "last123"
    assert collection.has_more is False

    assert not collection.has_next_page()
    assert not collection.has_next_cursor()
    assert collection.is_last_page()


def test_last_page_without_cursor() -> None:
    collection = DummyVantageCollection({
        "data": [],
        "meta": {
            "count": 0,
            "cursor": None,
            "hasMore": False,
        },
    })

    assert collection.meta_count == 0
    assert collection.cursor is None
    assert collection.is_last_page()


def test_defaults_to_empty_collection() -> None:
    collection = DummyVantageCollection({
        "meta": {
            "count": 0,
            "hasMore": False,
        },
    })

    assert collection.items == []
    assert len(collection) == 0
    assert list(collection) == []


def test_meta_count_is_independent_of_collection_length() -> None:
    collection = DummyVantageCollection({
        "data": [],
        "meta": {
            "count": 10,
            "cursor": None,
            "hasMore": False,
        },
    })

    assert collection.meta_count == 10
    assert len(collection) == 0


@pytest.mark.parametrize(
    "meta",
    [
        None,
        [],
        "invalid",
        123,
    ],
)
def test_rejects_invalid_metadata(meta: object) -> None:
    with pytest.raises(
        ValueError,
        match="Vantage pagination metadata is missing",
    ):
        DummyVantageCollection({
            "data": [],
            "meta": meta,
        })


def test_rejects_missing_metadata() -> None:
    with pytest.raises(
        ValueError,
        match="Vantage pagination metadata is missing",
    ):
        DummyVantageCollection({"data": []})


@pytest.mark.parametrize(
    ("meta", "missing_field"),
    [
        ({"hasMore": False}, "count"),
        ({"count": 10}, "hasMore"),
        ({}, "count"),
    ],
)
def test_rejects_missing_required_fields(
    meta: dict[str, object],
    missing_field: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=f"Missing Vantage pagination field: {missing_field}",
    ):
        DummyVantageCollection({
            "data": [],
            "meta": meta,
        })


@pytest.mark.parametrize(
    "count",
    [
        -1,
        "10",
        1.5,
        True,
        None,
    ],
)
def test_rejects_invalid_count(count: object) -> None:
    with pytest.raises(
        TypeError,
        match=r"Expected 'meta\.count' to be a non-negative integer",
    ):
        DummyVantageCollection({
            "data": [],
            "meta": {
                "count": count,
                "hasMore": False,
            },
        })


@pytest.mark.parametrize(
    "has_more",
    [
        "true",
        1,
        None,
        [],
    ],
)
def test_rejects_invalid_has_more(has_more: object) -> None:
    with pytest.raises(
        TypeError,
        match="Expected 'has_more' to be a boolean",
    ):
        DummyVantageCollection({
            "data": [],
            "meta": {
                "count": 10,
                "hasMore": has_more,
            },
        })


@pytest.mark.parametrize(
    "cursor",
    [
        123,
        True,
        [],
        {},
    ],
)
def test_rejects_invalid_cursor(cursor: object) -> None:
    with pytest.raises(
        TypeError,
        match="Expected 'next_cursor' to be a string or None",
    ):
        DummyVantageCollection({
            "data": [],
            "meta": {
                "count": 10,
                "cursor": cursor,
                "hasMore": True,
            },
        })


@pytest.mark.parametrize("cursor", [None, ""])
def test_requires_cursor_when_more_results_exist(
    cursor: str | None,
) -> None:
    with pytest.raises(
        ValueError,
        match="'next_cursor' must be provided",
    ):
        DummyVantageCollection({
            "data": [],
            "meta": {
                "count": 10,
                "cursor": cursor,
                "hasMore": True,
            },
        })


def test_rejects_invalid_collection_data() -> None:
    with pytest.raises(
        TypeError,
        match="Expected 'data' to be a list, got dict",
    ):
        DummyVantageCollection({
            "data": {"id": 1},
            "meta": {
                "count": 1,
                "hasMore": False,
            },
        })
