# class for n*m matrices
import math
from typing import Tuple


class Matrix:
    def __init__(self, *coords: Tuple[float]) -> None:
        Matrix.__check_len(coords)
        self.coords: Tuple[float] = tuple(coords)

    @property
    def determinant():
        pass

    def __str__():
        pass

    def __repr__(self):
        return "Not implemented"

    def __add__():
        pass

    def __neg__():
        pass

    def __sub__():
        pass

    def __mul__():
        pass

    def __rmul__():
        pass

    def __matmul__():
        pass

    def __truediv__():
        pass

    def __pow__():
        pass

    def to_int():
        pass

    def to_float():
        pass

    def is_zero():
        pass

    def is_one():
        pass

    def is_diagonal():
        pass

    def is_symmetric():
        pass

    def is_antisymmetric():
        pass

    def transpose():
        """in place"""
        pass

    def gauss_method():
        pass

    def gauss_reversed():
        pass

    def gauss(self):
        self.gauss_method()
        self.gauss_reversed()

    @classmethod
    def orlata(a, b):  # search the name in english
        pass

    @classmethod
    def get_transposed():
        """not in place"""
        pass

    @classmethod
    def identity():
        pass

    @classmethod
    def invert():
        pass

    @staticmethod
    def size(matrix: object):
        pass

    @staticmethod
    def have_same_size():
        pass

    @staticmethod
    def __check_len(coords):
        if len(coords) == 0:
            raise TypeError("Matrices should have at least one row")
        n_elements = len(coords[0])
        for row in coords:
            if (len_row := len(row)) == 0:
                raise TypeError("Each row should have at least one element in a matrix")
            for value in row:
                if isinstance(value, int | float):
                    continue
                raise TypeError("Matrices values can only be integers or floats")

            if n_elements == len_row:
                continue
            raise TypeError(
                "Matrices should have the same number of elements in each row"
            )
