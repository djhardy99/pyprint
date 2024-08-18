"""
Entrypoint, public facing API
"""

from typing import Any

from pyprint.components import pyprint_dict, pyprint_item, pyprint_list, pyprint_set


def pyprint(item: Any, return_str: bool = False) -> str | None:
    """
    pyprint is a helper method will take an input variable, and prettify it for print output.

    Args:
      item: (any) The item you wish to print
      return_str: (bool) Default is False. If True, will return the ASCII encoded string instead of printing the output
    """
    # None case
    if (
        item is None
        or isinstance(item, int)
        or isinstance(item, float)
        or isinstance(item, complex)
        or isinstance(item, str)
        or isinstance(item, bool)
        or isinstance(item, bytes)
    ):
        return pyprint_item(item, return_str)
    # Dict
    if isinstance(item, dict):
        return pyprint_dict(item, return_str)
    # Lists
    if isinstance(item, list):
        return pyprint_list(item, return_str)
    # Sets
    if isinstance(item, set):
        return pyprint_set(item, return_str)
    # Base case for edge cases not covered so far
    if return_str:
        return str(item)
    print(item)
