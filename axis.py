from enum import Enum


class Axis(Enum):
    """possible row axis on cartesian board. Row, Column, Diagonals.
    Main Diagonal means "top left to bottom right", Anti Diagonal means "bottom left to top right"
    """

    ROW = 0
    COL = 1
    MAINDIAG = 2
    ANTIDIAG = 3
