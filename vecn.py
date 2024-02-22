import math
from typing import List, Tuple


# abstract class for vectors of dimension n
class Vector:
    def __init__(self, *coords: Tuple[float]) -> None:
        if len(coords) == 0:
            raise TypeError(
                "Vector objects must have at least 1 argument, 0 where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: List[float] = list(coords)

    def __repr__(self) -> str:
        return (
            f"Vec{self.coords.__len__()}D("
            + ", ".join(str(coord) for coord in self.coords)
            + ")"
        )

    def __len__(self) -> int:
        return len(self.coords)

    def __add__(self, other: object) -> object:
        Vector.__check_raise_same_dim_error(self, other)
        return type(self)(*(a + b for a, b in zip(self.coords, other.coords)))

    def __neg__(self) -> object:
        return type(self)(*(-coord for coord in self.coords))

    def __sub__(self, other: object) -> object:
        Vector.__check_raise_same_dim_error(self, other)
        return type(self)(*(a - b for a, b in zip(self.coords, other.coords)))

    def __mul__(self, other: float | object) -> object | float:
        if isinstance(other, int | float):
            return type(self)(*(other * coord for coord in self.coords))
        if isinstance(other, Vector):
            Vector.__check_raise_same_dim_error(self, other)
            return sum(list(a * b for a, b in zip(self.coords, other.coords)))
        raise TypeError("Tried multiplying a vector with a non numerical value")

    def __rmul__(self, other: object) -> object | float:
        return self * other

    def __truediv__(self, other: object) -> object:
        if not isinstance(other, int | float):
            raise TypeError("Tried dividing a vector with a non numerical value")
        if other == 0:
            raise ZeroDivisionError("Tried dividing a vector for zero")
        return self * (1 / other)

    def __pow__(self, other: int) -> object | float:
        if not isinstance(other, int):
            raise TypeError("The exponent must be an integer")
        if other < 0:
            raise ValueError("The exponent must be positive or zero")
        if other == 0:
            if self.is_zero():
                raise ValueError("Cannot raise a zero vector to the power of zero")
            return 1
        if other == 1:
            return self
        return self * self ** (other - 1)

    def is_zero(self) -> bool:
        return not any(self.coords)

    def get_cartesian_coordinates(self) -> Tuple[float]:
        return tuple(coord for coord in self.coords)

    @property
    def module(self) -> float:
        return math.hypot(*self.coords)

    @staticmethod
    def have_same_dimension(x: object, y: object) -> bool:
        return len(x) == len(y)

    @staticmethod
    def __check_raise_same_dim_error(x: object, y: object) -> None:
        if not Vector.have_same_dimension(x, y):
            raise TypeError(
                f"Vectors must have the same dimension\n\t"
                + f"instead got: vec{len(x)}D and vec{len(y)}D"
            )
