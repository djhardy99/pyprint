"""
This contains the logic for validators, made for reuse by other methods
"""

from typing import List

from pyprint.colors import Colors, Styles


def validate_style_list(styles: List[str]):
    if not isinstance(styles, list):
        raise TypeError(
            f"styles param must be a list of valid strings belonging to the pyprint.colors.Styles class, but was instead a {type(styles)} of value {styles}"
        )
    if len(styles) != 0:
        # If the styles list is empty, we don't need to test anything else here
        for style in styles:
            validate_style(style)


def validate_style(style: str):
    if not isinstance(style, str):
        raise TypeError(
            f"style param must be a valid string belonging to the pyprint.colors.Styles class, but was instead a {type(style)} of value {style}"
        )
    if not Styles._is_style_code_valid(style):
        raise ValueError(
            f"style param must be a valid string belonging to the pyprint.colors.Styles class, but was instead {style}. Pass in a Styles property to address this."
        )


def validate_color(color: str):
    if not isinstance(color, str):
        raise TypeError(
            f"color param must be a valid string belonging to the pyprint.colors.Colors class, but was instead a {type(color)} of value {color}"
        )
    if not Colors._is_color_code_valid(color):
        raise ValueError(
            f"color param must be a valid string belonging to the pyprint.colors.Colors class, but was instead {color}. Pass in a Colors property to address this."
        )


def validate_char(char: str):
    if not isinstance(char, str):
        raise TypeError(
            f"icon param must be a string with a length of one, but was instead a {type(char)} of value {char}"
        )
    if not len(char) == 1:
        raise ValueError(
            f"icon param must be a string with length of one, but instead had a length of {len(char)} for the value {char}"
        )


def validate_string(text: str):
    if not isinstance(text, str):
        raise TypeError(
            f"Param must be a string, but was instead a {type(text)} of value {text}"
        )
