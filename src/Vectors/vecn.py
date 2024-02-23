import copy
import math
from typing import Tuple


class Vector:
    """class for a n-dimensional vector"""

    def __init__(self, *coords: float) -> None:
        """Create an object from an unpacked tuple of coordinates"""
        if len(coords) == 0:
            raise TypeError(
                "Vector objects must have at least 1 argument, 0 where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: tuple[float] = tuple(coords)

    @property
    def module(self) -> float:
        """return the modulus of the vector, which is the euclidean norm in n dimensions"""
        return math.hypot(*self.coords)

    def __repr__(self) -> str:
        """return a string in the form of Vec{dimension}D{tuple of the coordinates}"""
        return (
            f"Vec{self.coords.__len__()}D("
            + ", ".join(str(coord) for coord in self.coords)
            + ")"
        )

    def __len__(self) -> int:
        """return the length of the Vector (the number of dimensions)"""
        return len(self.coords)

    def __add__(self, other: object) -> object:
        """definition of addition"""
        Vector.__check_raise_same_dim_error(self, other)
        return type(self)(*(a + b for a, b in zip(self.coords, other.coords)))

    def __neg__(self) -> object:
        """definition of negation"""
        return type(self)(*(-coord for coord in self.coords))

    def __sub__(self, other: object) -> object:
        """definition of subtraction"""
        Vector.__check_raise_same_dim_error(self, other)
        return type(self)(*(a - b for a, b in zip(self.coords, other.coords)))

    def __mul__(self, other: float | object) -> object | float:
        """definition of inner product, and product for scalar"""
        if isinstance(other, int | float):
            return type(self)(*(other * coord for coord in self.coords))
        if isinstance(other, Vector):
            Vector.__check_raise_same_dim_error(self, other)
            return sum(list(a * b for a, b in zip(self.coords, other.coords)))
        raise TypeError("Tried multiplying a vector with a non numerical value")

    def __rmul__(self, other: object) -> object | float:
        """definition of product for scalar"""
        return self * other

    def __truediv__(self, other: object) -> object:
        """definition of division by scalar"""
        if not isinstance(other, int | float):
            raise TypeError("Tried dividing a vector with a non numerical value")
        if other == 0:
            raise ZeroDivisionError("Tried dividing a vector for zero")
        return self * (1 / other)

    def __pow__(self, other: int) -> object | float:
        """definition of integer power"""
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
        """check if the vector is a zero vector

        Returns:
            bool: true if the vector is in the form of Vector(0, 0, ...), false otherwise
        """
        return not any(self.coords)

    def get_cartesian_coordinates(self) -> Tuple[float]:
        """return the cartesian coordinates of the vector as a tuple"""
        return tuple(coord for coord in self.coords)

    # ? I don't know if it's better to make it a staticmethod or leave it as it is
    # ! I should do more tests to see if this is a real deepcopy or if this creates a bug
    def copy(self):
        """return a deepcopy of the vector"""
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
        """Use a matrix to transform the coordinates"""
        pass

    def normalize(self) -> None:
        """Normalize inplace the vector.

        The vector components are divided by the modulus to get a vector with
        same direction but modulus one.

        Raises:
            ValueError: if the vector is a zero vector, it's not defined the normalization.
        """
        if self.is_zero():
            raise ValueError("Cannot normalize a zero vector")
        self.coords[::] = [coord / self.module for coord in self.coords]

    def get_normalized(self) -> object:
        """return the normalized vector (not inplace)

        The vector components are divided by the modulus to get a vector with
        same direction but modulus one.

        Raises:
            ValueError: if the vector is a zero vector, it's not defined the normalization.

        Returns:
            object: a new Vector (or subclass), it always has modulus 1.
        """
        if self.is_zero():
            raise ValueError("Cannot normalize a zero vector")
        return type(self)(*[coord / self.module for coord in self.coords])

    def create_parallel(self, module: float) -> object:
        """Creates a new Vector (or subclass) with same direction and verse but different modulus

        Args:
            module (float): the modulus of the new vector

        Raises:
            ValueError: the modulus should always be positive or zero

        Returns:
            object: a new Vector (or subclass)
        """
        if not isinstance(module, int | float):
            raise ValueError(
                "The module of the new vector should be a float or integer"
            )
        return self.get_normalized() * module

    # TODO NOTE
    def shorten_to(self, other: object) -> object:
        pass

    # TODO
    def stretch_to(self, other: object) -> object:
        pass

    # TODO
    @staticmethod
    def shorten_to_minimum_length(*vectors: object) -> Tuple[object]:
        pass

    # TODO
    @staticmethod
    def stretch_to_maximum_length(
        *vectors: object, default: float = 0
    ) -> Tuple[object]:
        pass

    @staticmethod
    def have_same_dimension(a: object, b: object) -> bool:
        """Return true if the arguments have the same length, false otherwise"""
        if not isinstance(a, Vector) or not isinstance(b, Vector):
            raise TypeError("Both arguments should be Vector")
        return len(a) == len(b)

    @staticmethod
    def distance(a: object, b: object) -> float:
        """return the euclidean distance of two vectors"""
        if not isinstance(a, Vector) or not isinstance(b, Vector):
            raise TypeError("Both arguments should be Vector")
        return (b - a).module

    @staticmethod
    def __check_raise_same_dim_error(x: object, y: object) -> None:
        """raise an error if the vectors don't have the same length"""
        if not Vector.have_same_dimension(x, y):
            raise TypeError(
                f"Vectors must have the same dimension\n\t"
                + f"instead got: vec{len(x)}D and vec{len(y)}D"
            )
