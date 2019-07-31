import re


class UnitError(Exception):
    """Not unit in the line"""


def conversion(data: str) -> float:
    if "km" not in data and "mi" not in data:
        raise UnitError("Add km or mi in data line.")

    count = re.search(r"\d+(?:\.\d+)?", data).group(0)
    if "km" in data:
        convert = 0.621371 * float(count)
    else:
        convert = 1.60934 * float(count)
    convert = round(convert, 2)
    return convert
