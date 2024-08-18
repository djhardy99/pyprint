"""
Contains the ASCII styles lookup class
"""

from functools import cache


class Styles:
    """
    A class containing ANSI escape codes for styling text in terminal output.

    This class provides constants for various text styles that can be used
    to format terminal output.

    Attributes:
        Style Attributes:
            default (str): This is a default value for your terminals normal output
            reset (str): Resets all styles and colors to default.
            bold (str): Applies bold text style.
            disable (str): Applies dim text style.
            underline (str): Applies underline text style.
            reverse (str): Applies reverse video text style.
            strikethrough (str): Applies strikethrough text style.
            invisible (str): Applies invisible text style.

    Example:
        To use these styles and colors in terminal output:
        ```
        print(Colors.bold + 'This is bold text' + Colors.reset)
        ```

    Notes:
        The escape codes provided are ANSI codes and may not be supported on all terminal emulators.
    """

    # Base
    default = ""  # This is here as a default value for methods, will render as the terminals default text color
    reset = "\033[0m"
    # Styling
    bold = "\033[01m"
    italics = "\033[03m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    @classmethod
    @cache
    def _is_style_code_valid(cls, value: str):
        """
        Check if the given value is a valid color code defined in the Style class.
        This is an internal method used for validation.

        Args:
            value (str): The style code string to check.

        Returns:
            bool: True if the value matches any of the color codes, False otherwise.
        """
        # Extract all attributes of the Style class
        style_codes = vars(cls).values()

        # Check if the value is in the list of style codes
        return value in style_codes
