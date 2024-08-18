"""
Contains the ASCII colours lookup class
"""

from functools import cache


class Colors:
    """
    A class containing ANSI escape codes for coloring text in terminal output.

    This class provides constants for various text colors that can be used
    to format terminal output. Access members as class properties. Foreground colors are
    accessed by their standard names (e.g., `Colors.red`), while background colors are
    accessed with the `_bg` suffix (e.g., `Colors.red_bg`).

        Foreground Color Attributes:
            default (str): This is a default value for your terminals normal output
            black (str): Text color black.
            red (str): Text color red.
            green (str): Text color green.
            orange (str): Text color orange.
            blue (str): Text color blue.
            purple (str): Text color purple.
            cyan (str): Text color cyan.
            lightgrey (str): Text color light grey.
            darkgrey (str): Text color dark grey.
            lightred (str): Text color light red.
            lightgreen (str): Text color light green.
            yellow (str): Text color yellow.
            lightblue (str): Text color light blue.
            pink (str): Text color pink.
            lightcyan (str): Text color light cyan.

        Background Color Attributes:
            black_bg (str): Background color black.
            red_bg (str): Background color red.
            green_bg (str): Background color green.
            orange_bg (str): Background color orange.
            blue_bg (str): Background color blue.
            purple_bg (str): Background color purple.
            cyan_bg (str): Background color cyan.
            lightgrey_bg (str): Background color light grey.

    Example:
        To use these styles and colors in terminal output:
        ```
        print(Colors.red + 'This is red text' + Colors.reset)
        print(Colors.blue_bg + Colors.white + 'This is text on a blue background' + Colors.reset)
        ```

    Notes:
        The escape codes provided are ANSI codes and may not be supported on all terminal emulators.
    """

    # Base
    reset = "\033[0m"
    default = ""  # This is here as a default value for methods, will render as the terminals default text color

    # Foreground
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    lightgrey = "\033[37m"
    darkgrey = "\033[90m"
    lightred = "\033[91m"
    lightgreen = "\033[92m"
    yellow = "\033[93m"
    lightblue = "\033[94m"
    pink = "\033[95m"
    lightcyan = "\033[96m"

    # Background
    black_bg = "\033[40m"
    red_bg = "\033[41m"
    green_bg = "\033[42m"
    orange_bg = "\033[43m"
    blue_bg = "\033[44m"
    purple_bg = "\033[45m"
    cyan_bg = "\033[46m"
    lightgrey_bg = "\033[47m"

    @classmethod
    @cache
    def _is_color_code_valid(cls, value: str):
        """
        Check if the given value is a valid color code defined in the Colors class.
        This is an internal method used for validation.

        Args:
            value (str): The color code string to check.

        Returns:
            bool: True if the value matches any of the color codes, False otherwise.
        """
        # Extract all attributes of the Colors class
        color_codes = vars(cls).values()

        # Check if the value is in the list of color codes
        return value in color_codes
