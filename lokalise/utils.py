"""
lokalise.utils
~~~~~~~~~~~~~~
This module contains various utility functions.
"""
from typing import Union, List, Dict


def snake_to_camel(word: str) -> str:
    """Converts string in snake case to camel case.
    For example, "test_string" becomes "TestString"
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def to_list(obj: Union[List, Dict]) -> List:
    """Converts a dictionary to list. If the object is already a list,
    does nothing.

    :param obj: Object to convert
    :type obj: list or dict
    """
    return [obj] if isinstance(obj, dict) else obj
