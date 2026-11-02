
"""
Tests for the base collection.
"""

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


def test_defaults_to_empty_collection() -> None:
    collection = DummyCollection({})

    assert collection.items == []
    assert len(collection) == 0
    assert list(collection) == []


def test_builds_models() -> None:
    collection = DummyCollection({
        "items": [
            {"id": 1},
            {"id": 2},
        ],
    })

    assert len(collection) == 2
    assert all(isinstance(item, BaseModel) for item in collection)


def test_supports_indexing_and_slicing() -> None:
    collection = DummyCollection({
        "items": [
            {"id": 1},
            {"id": 2},
            {"id": 3},
        ],
    })

    assert collection[0] is collection.items[0]
    assert collection[-1] is collection.items[-1]
    assert collection[1:] == collection.items[1:]
    assert list(collection) == collection.items


def test_ignores_unrelated_response_fields() -> None:
    collection = DummyCollection({
        "items": [],
        "meta": {"count": 10},
        "_pagination": "invalid",
    })

    assert collection.items == []
