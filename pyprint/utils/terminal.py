"""
Terminal utils
"""

import os

from pyprint.colors import Colors, Styles


def get_all_colors(return_str: bool = False) -> str:
    """
    This function is designed around displaying all possible colours in your terminal, so to see how things look with your IDE theme.
    Returns:
        str: Formatted string designed around printing in the terminal
    """
    colors_attributes = {
        name: value for name, value in vars(Colors).items() if not name.startswith("_")
    }
    styles_attributes = {
        name: value for name, value in vars(Styles).items() if not name.startswith("_")
    }
    all_attributes = {**colors_attributes, **styles_attributes}
    tempList = []
    for name, value in all_attributes.items():
        tempList.append(f"{value}{name}{Colors.reset}")
    colString: str = "\n".join(tempList)
    if return_str:
        return colString
    print(colString)


def get_term_width() -> int:
    """
    Util function to get terminal size, or get default size of 88 in case of error
    Returns:
        int: width of terminal
    """
    try:
        width: int = os.get_terminal_size().columns
    except:
        width: int = (
            88  # If there is an error due to integrated terminals, debuggers etc such as within Pycharm
        )
    return width
