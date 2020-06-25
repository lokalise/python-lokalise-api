"""
lokalise.utils
~~~~~~~~~~~~~~
This module contains various utility functions.
"""
from typing import List, Any


def snake_to_camel(word: str) -> str:
    """Converts string in snake case to camel case.
    For example, "test_string" becomes "TestString"
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def to_list(obj: Any) -> List:
    """Converts an object to a list. If the object is already a list,
    does nothing.

    :param obj: Object to convert
    """
    return obj if isinstance(obj, list) else [obj]
