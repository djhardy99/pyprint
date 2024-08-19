"""
Terminal utils
"""

import os


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
