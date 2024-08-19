from pyprint.colors.colors import Colors
from pyprint.colors.styles import Styles
from pyprint.components import (
    pyprint_header,
    pyprint_subheader,
    pyprint_subfooter,
    pyprint_footer,
)


def get_all_colors(return_str: bool = False) -> str | None:
    """
    This function is designed around displaying all possible colours in your terminal, so to see how things look with your IDE theme.
    Returns:
        str: Formatted string designed around printing in the terminal
    """
    header = pyprint_header("PyPrint ASCII Codes", return_str=True)
    subheader_colors = pyprint_subheader("PyPrint Colors", return_str=True)
    subheader_styles = pyprint_subheader("PyPrint Styles", return_str=True)
    subfooter = pyprint_subfooter(return_str=True)
    footer = pyprint_footer(return_str=True)
    colors_attributes = {
        name: value for name, value in vars(Colors).items() if not name.startswith("_")
    }
    styles_attributes = {
        name: value for name, value in vars(Styles).items() if not name.startswith("_")
    }
    tempList = []
    tempList.append(header)
    tempList.append(subheader_colors)
    for name, value in colors_attributes.items():
        tempList.append(f"{value}{name}{Colors.reset}")
    tempList.append(subfooter)
    tempList.append(subheader_styles)
    for name, value in styles_attributes.items():
        tempList.append(f"{value}{name}{Colors.reset}")
    tempList.append(subfooter)
    tempList.append(footer)
    colString: str = "\n".join(tempList)
    if return_str:
        return colString
    print(colString)
