"""
lokalise.utils
~~~~~~~~~~~~~~
This module contains various utility functions.
"""


def snake_to_camel(word):
    """Converts string in snake case to camel case.
    For example, "test_string" becomes "TestString"
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
