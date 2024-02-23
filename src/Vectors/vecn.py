import math
from typing import List, Tuple


class Vector:
    def __init__(self, *coords: Tuple[float]) -> None:
        if len(coords) == 0:
            raise TypeError(
                "Vector objects must have at least 1 argument, 0 where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: List[float] = list(coords)

    @property
    def module(self) -> float:
        return math.hypot(*self.coords)

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

    # ? should I use is_similar()?
    def is_zero(self) -> bool:
        return not any(self.coords)

    def get_cartesian_coordinates(self) -> Tuple[float]:
        return tuple(coord for coord in self.coords)

    # ? I don't know if it's better to make it a staticmethod or leave it as it is
    def copy(self):
        return type(self)(*(coord for coord in self.coords))

    def translate(self, origin: object):
        """In place tanslation

        Args:
            origin (object): the new origin in current coordinates
        """
        if not isinstance(origin, Vector):
            raise ValueError("The origin of the translation should be a Vector")
        Vector.__check_raise_same_dim_error(self, origin)
        self.coords[::] = [x + y for x, y in zip(self.coords, (-origin).coords)]

    # TODO after implementing matrices
    def transform_coords(self, eigen_vector: object):
        pass

    def normalize(self) -> None:
        """Normalize in place the vector

        Raises
        ------
        ValueError
            if the vector is a zero vector, the normalized vector it's not defined
        """
        if self.is_zero():
            raise ValueError("Cannot normalize a zero vector")
        self.coords[::] = [coord / self.module for coord in self.coords]

    def get_normalized(self) -> object:
        """Return the normalized vector as a new object

        Returns
        -------
        object
            The normalized vector, it's type it's the same as the vector given

        Raises
        ------
        ValueError
            if the vector is a zero vector, the normalized vector it's not defined
        """
        if self.is_zero():
            raise ValueError("Cannot normalize a zero vector")
        return type(self)(*[coord / self.module for coord in self.coords])

    def create_parallel(self, module: float = 1) -> object:
        """Crate a new object parallel to the instance and with a specified module

        Parameters
        ----------
        module : float, optional
            the module the new vector has to be, by default 1

        Returns
        -------
        object
            a new instance it's returned the same type as self
        """
        if not isinstance(module, int | float):
            raise ValueError(
                "The module of the new vector should be a float or integer"
            )
        return self.get_normalized() * module

    # TODO
    def shorten_to(self, other):
        pass

    # TODO
    def stretch_to(self, other):
        pass

    # TODO
    @staticmethod
    def shorten_to_minimum_length(a, b):  # ? should I use an iterable?
        pass

    # TODO
    @staticmethod
    def stretch_to_maximum_length(a, b):
        pass

    @staticmethod
    def have_same_dimension(a: object, b: object) -> bool:
        if not isinstance(a, Vector) or not isinstance(b, Vector):
            raise TypeError("Both arguments should be Vector")
        return len(a) == len(b)

    @staticmethod
    def distance(a: object, b: object) -> float:
        if not isinstance(a, Vector) or not isinstance(b, Vector):
            raise TypeError("Both arguments should be Vector")
        return (b - a).module

    @staticmethod
    def __check_raise_same_dim_error(x: object, y: object) -> None:
        if not Vector.have_same_dimension(x, y):
            raise TypeError(
                f"Vectors must have the same dimension\n\t"
                + f"instead got: vec{len(x)}D and vec{len(y)}D"
            )
