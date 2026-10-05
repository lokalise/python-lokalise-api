"""
lokalise.utils
~~~~~~~~~~~~~~
This module contains various utility functions.
"""

from typing import TypeVar, cast

T = TypeVar("T")


def snake_to_camel(word: str) -> str:
    """Converts string in snake case to camel case.
    For example, "test_string" becomes "TestString"
    """
    return "".join(x.capitalize() or "_" for x in word.split("_"))


def to_list(obj: T | list[T]) -> list[T]:
    """Converts an object to a list. If the object is already a list,
    does nothing.

    :param obj: Object to convert
    """
    return cast(list[T], obj) if isinstance(obj, list) else [obj]
