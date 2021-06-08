from pygments.style import Style
from pygments.token import (Comment, Error, Generic, Keyword, Name, Number,
                            Operator, String)

FIT_LBLUE = "#00A9E0"
FIT_GRAY = "#808080"
FIT_LGRAY = "#E5E5E5"
FIT_BLUE = "#007BA3"
FIT_DBLUE = "#0B132B"
FIT_RED = "#E4002B"


class FitStyle(Style):
    default_style = ""
    styles = {
        Comment: f"italic {FIT_LGRAY}",
        Keyword: f"bold {FIT_LBLUE}",
        Name.Variable: f"{FIT_BLUE}",
        String.Double: f"{FIT_RED}",
        String.Regex: f"{FIT_RED}",
    }
