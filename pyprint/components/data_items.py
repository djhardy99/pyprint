"""
This contains the logic for printing each 'primitive' data type.

Currently supports:

Text Type: str
Numeric Types: int, float, complex
Boolean Type: bool
Binary Types: bytes
None Type: NoneType
"""

from typing import Any

from pyprint.colors import Colors

COLOR_LOOKUP_MAP = {
    "none": Colors.purple,
    "number_key": Colors.cyan,
    "number_value": Colors.lightcyan,
    "string_key": Colors.yellow,
    "string_value": Colors.lightblue,
    "boolean_true": Colors.lightgreen,
    "boolean_false": Colors.lightred,
    "bytes_key": Colors.green,
    "bytes_value": Colors.lightblue,
}


def get_dtype_colors(item: Any, is_key: bool = False) -> str:
    """
    Returns a color for the items value.
    for dictionaries, key-value types will have a different colors for some data types
    This function is designed for single items, any lists / groupings etc will be handled elsewhere
    """
    MISSING_VAR = "ERROR"
    # None case
    if item is None:
        # Will use purple for both key and value
        return COLOR_LOOKUP_MAP.get("none", MISSING_VAR)
    if isinstance(item, bool):
        # Instead of key value, will give green / red for True / False
        if item:
            return COLOR_LOOKUP_MAP.get("boolean_true", MISSING_VAR)
        return COLOR_LOOKUP_MAP.get("boolean_false", MISSING_VAR)
    # Numerics
    if isinstance(item, int) or isinstance(item, float) or isinstance(item, complex):
        if is_key:
            return COLOR_LOOKUP_MAP.get("number_key", MISSING_VAR)
        return COLOR_LOOKUP_MAP.get("number_value", MISSING_VAR)
    # Strings
    if isinstance(item, str):
        if is_key:
            return COLOR_LOOKUP_MAP.get("string_key", MISSING_VAR)
        return COLOR_LOOKUP_MAP.get("string_value", MISSING_VAR)
    # Booleans
    # Bytes
    if isinstance(item, bytes):
        if is_key:
            return COLOR_LOOKUP_MAP.get("bytes_key", MISSING_VAR)
        return COLOR_LOOKUP_MAP.get("bytes_value", MISSING_VAR)
    else:
        # Base case for edge cases missed
        return MISSING_VAR


def pyprint_item(
    item: Any, return_str: bool = False, is_key: bool = False
) -> str | None:
    # Check if the item is a string and wrap it in quotes at the end (to get the colo)

    color: str = get_dtype_colors(item, is_key)
    item_str_colored: str = f"{color}{item}{Colors.reset}"

    if isinstance(item, str):
        colored_quotes = f'{Colors.darkgrey}"{Colors.reset}'
        item_str_colored = f"{colored_quotes}{item_str_colored}{colored_quotes}"

    if return_str:
        return item_str_colored
    print(item_str_colored)
