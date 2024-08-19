"""
This contains headers, footers, breakpoints and any other section markers that are separate from content specific output.
"""

from pyprint.colors import Colors, Styles
from .terminal_utils import get_term_width
from pyprint.components.validators import validate_string


def pyprint_header(text: str, return_str: bool = False) -> str | None:
    """
    Creates a major header section.
    This will be the length of the terminal this method is executed in.
    This contains a full banner surrounding the title

    Args:
        text (str): The text to display as the major header.
        return_str (bool): If True, will return the header string, if False, will print within the method. Default is False
    Returns:
        (str) Header string
    Example:
        =============== Introduction ===============
    """
    # Testing that all input parameters are valid
    validate_string(text)
    text_color = Colors.lightred
    icon = "="
    icon_color = Colors.orange
    width: int = get_term_width()
    title_w_padding: str = " " + text + " "
    side_banner_len: int = int((width - len(title_w_padding)) / (len(icon) * 2))
    side_banner: str = icon * side_banner_len
    styled_side_banner: str = Styles.bold + icon_color + side_banner + Colors.reset
    styled_title = Styles.bold + text_color + title_w_padding + Colors.reset
    header_styled: str = (
        styled_side_banner + styled_title + styled_side_banner + Colors.reset
    )
    if return_str:
        return header_styled
    print(header_styled)


def pyprint_subheader(text: str, return_str: bool = False) -> str | None:
    """
    Creates a minor header for the report.

    A minor header is used for subsections or detailed divisions within a major
    section. It is less prominent and helps to organize content into smaller
    segments within a major section, such as "Methodology" or "Data Analysis".

    Args:
        text (str): The text to display as the minor header.

    Example:
        --- Data Analysis ---
    """
    # Testing that all input parameters are valid
    validate_string(text)
    text_color = Colors.cyan
    icon = "-"
    icon_color = Colors.lightgrey
    width: int = get_term_width()
    title_w_padding: str = " " + text + " "
    side_banner_len: int = int((width - len(title_w_padding)) / (len(icon) * 2))
    side_banner: str = icon * side_banner_len
    styled_side_banner: str = Styles.italics + icon_color + side_banner + Colors.reset
    styled_title = Styles.italics + text_color + title_w_padding + Colors.reset
    header_styled: str = (
        styled_side_banner + styled_title + styled_side_banner + Colors.reset
    )
    if return_str:
        return header_styled
    print(header_styled)


def pyprint_footer(return_str: bool = False) -> str | None:
    width = get_term_width()
    icon = "="
    icon_color = Colors.orange
    footer_string = icon * int(width / len(icon))
    styled_footer = icon_color + footer_string + Colors.reset + "\n"
    if return_str:
        return styled_footer
    print(styled_footer)


def pyprint_subfooter(return_str: bool = False) -> str | None:
    width = get_term_width()
    icon = "_"
    icon_color = Colors.lightgrey
    footer_string = icon * int(width / len(icon))
    styled_footer = Styles.bold + icon_color + footer_string + Colors.reset
    if return_str:
        return styled_footer
    print(styled_footer)
