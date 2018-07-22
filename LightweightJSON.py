from typing import Mapping, Iterable
from uuid import UUID


def to_string(o: object) -> str:
    if isinstance(o, UUID):
        return to_string(str(o))

    if isinstance(o, str):
        return '"' + o + '"'

    if isinstance(o, Mapping):
        s = "{"
        multiple = False

        for x in o:
            if multiple:
                s += " , "

            s += '"' + x + '"' + " : " + to_string(o[x])
            multiple = True
        return s + "}"

    if isinstance(o, Iterable):
        s = "["
        multiple = False
        for x in o:
            if multiple:
                s += " , "
            s += to_string(x)
            multiple = True
        return s + "]"

    try:
        values = vars(o)
        s = "{"
        multiple = False

        for x in values:
            if multiple:
                s += " , "

            s += '"' + x + '"' + " : " + to_string(o.__getattribute__(x))
            multiple = True
        return s + "}"
    except TypeError:
        return to_string(str(o))
    pass
