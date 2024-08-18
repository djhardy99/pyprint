from typing import Any, Dict, List, Set

from pyprint.colors import Colors, Styles
from .data_items import pyprint_item


def pyprint_set(
    items: Set[Any], return_str: bool = False, level: int = 0
) -> str | None:
    indent = " " * (level * 2)
    braces_styling: str = Colors.lightgrey + Styles.italics
    str_start: str = braces_styling + "{" + Colors.reset
    str_end: str = braces_styling + "}" + Colors.reset
    list_items: List[str] = []

    for item in items:
        if isinstance(item, dict):
            item_str: str = pyprint_dict(items=item, return_str=True, level=level + 1)
        elif isinstance(item, list):
            item_str: str = pyprint_list(items=item, return_str=True, level=level + 1)
        elif isinstance(item, set):
            item_str: str = pyprint_set(items=item, return_str=True, level=level + 1)
        else:
            item_str: str = pyprint_item(item=item, return_str=True)
        list_items.append(item_str)

    str_items_styled: str = ",\n".join(f"{indent}  {item}" for item in list_items)
    return_str_item: str = f"{str_start}\n{str_items_styled}\n{indent}{str_end}"

    if return_str:
        return return_str_item
    print(return_str_item)


def pyprint_list(
    items: List[Any], return_str: bool = False, level: int = 0
) -> str | None:
    indent = " " * (level * 2)
    braces_styling: str = Colors.lightgrey + Styles.italics
    str_start: str = braces_styling + "[" + Colors.reset
    str_end: str = braces_styling + "]" + Colors.reset
    list_items: List[str] = []

    for item in items:
        if isinstance(item, dict):
            item_str: str = pyprint_dict(items=item, return_str=True, level=level + 1)
        elif isinstance(item, list):
            item_str: str = pyprint_list(items=item, return_str=True, level=level + 1)
        elif isinstance(item, set):
            item_str: str = pyprint_set(items=item, return_str=True, level=level + 1)
        else:
            item_str: str = pyprint_item(item=item, return_str=True)
        list_items.append(item_str)

    str_items_styled: str = ",\n".join(f"{indent}  {item}" for item in list_items)
    return_str_item: str = f"{str_start}\n{str_items_styled}\n{indent}{str_end}"

    if return_str:
        return return_str_item
    print(return_str_item)


def pyprint_dict(
    items: Dict[Any, Any], return_str: bool = False, level: int = 0
) -> str | None:
    indent = " " * (level * 2)
    braces_styling: str = Colors.lightgrey + Styles.italics
    str_start: str = braces_styling + "{" + Colors.reset
    str_end: str = braces_styling + "}" + Colors.reset
    return_str_list: List[str] = []
    colon_section = Colors.yellow + " : " + Colors.reset

    for key, value in items.items():
        key_str: str = pyprint_item(item=key, return_str=True, is_key=True)

        if isinstance(value, dict):
            value_str: str = pyprint_dict(items=value, return_str=True, level=level + 1)
        elif isinstance(value, list):
            value_str: str = pyprint_list(items=value, return_str=True, level=level + 1)
        elif isinstance(value, set):
            value_str: str = pyprint_set(items=value, return_str=True, level=level + 1)
        else:
            value_str: str = pyprint_item(item=value, return_str=True, is_key=False)

        return_str_list.append(f"{indent}  {key_str}{colon_section} {value_str}")

    return_str_item: str = (
        f"{str_start}\n{'\n'.join(return_str_list)}\n{indent}{str_end}"
    )

    if return_str:
        return return_str_item
    print(return_str_item)
