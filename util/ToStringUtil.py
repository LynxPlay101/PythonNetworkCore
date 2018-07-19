from typing import List


def or_else(string: str, replace: str) -> str:
    return string is None and replace or string


def from_list(l: List[object]) -> str:
    result = ""
    for x in l:
        result += x.__str__()
    return result
