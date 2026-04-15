from enum import StrEnum


class ScrollBlock(StrEnum):
    START = "start"
    CENTER = "center"
    END = "end"
    NEAREST = "nearest"