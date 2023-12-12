from enum import Enum


class Direction(Enum):

    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)
    NONE = (0, 0)
