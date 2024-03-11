import math
from typing import Tuple

from .matnm import Matrix


class SMatrix(Matrix):
    def __init__(self, *coords: Tuple[float]) -> None:
        SMatrix.__check_len(coords)
        self.coords: Tuple[float] = tuple(coords)

    @property
    def trace():
        pass

    @staticmethod
    def __check_len(coords):
        if (n_rows := len(coords)) == 0:
            raise TypeError("Matrices should have at least one row")
        n_elements = len(coords[0])
        for row in coords:
            if (len_row := len(row)) == 0:
                raise TypeError("Each row should have at least one element in a matrix")
            for value in row:
                if isinstance(value, int | float):
                    continue
                raise TypeError("Matrices values can only be integers or floats")

            if n_elements != len_row:
                raise TypeError(
                    "Matrices should have the same number of elements in each row"
                )
            if len_row != n_rows:
                raise TypeError(
                    "Square matrices should have the same number of columns and rows"
                )
