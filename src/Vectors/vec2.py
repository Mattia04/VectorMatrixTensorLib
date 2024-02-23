import cmath
import math
from typing import List, Tuple

from .vecn import Vector


class Vec2(Vector):
    def __init__(self, *coords: Tuple[float]) -> None:
        if len(coords) != 2:
            raise TypeError(
                f"Vector objects must have 2 argument, {len(coords)} where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: List[float] = list(coords)

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def phase(self) -> float:
        if self.is_zero():
            raise ValueError("The phase of a zero vector it's undefined")
        return cmath.phase(complex(self.x, self.y))

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -self + other

    def get_polar_coord(self) -> Tuple[float]:
        return self.module, self.phase

    def project_tangent(self, other: object) -> object:
        """Get the tangent component of other on self

        Parameters
        ----------
        other : object

        Returns
        -------
        object
            The projection vector of other on self

        Raises
        ------
        TypeError
            if other is not a Vec2
        """
        if not isinstance(other, Vec2):
            raise TypeError("To make a projection both vectors must be Vec2D")
        return (
            self.get_normalized()
            * other.module
            * math.cos(Vec2.get_angle_between(self, other))
        )

    def project_normal(self, other: object) -> object:
        """Get the normal vector of other on self

        Args:
            other (object): another Vec2

        Raises:
            TypeError: if other is not Vec2

        Returns:
            object: The projection vector of other on self
        """
        if not isinstance(other, Vec2):
            raise TypeError("To make a projection both vectors must be Vec2D")
        return other - self.project_tangent(other)

    def project_components(self, other: object) -> Tuple[object]:
        """get both projection of other on self

        Args:
            other (object): another Vec2

        Returns:
            Tuple[object]: Two Vec2
                the first is the Tangent component and the second is the normal
        """
        return self.project_tangent(other), self.project_normal(other)

    @classmethod
    def from_complex(cls, num: complex) -> object:
        if not isinstance(num, complex):
            raise TypeError("Argument should be a complex number")
        return Vec2(num.real, num.imag)

    @classmethod
    def from_polar(cls, rho: float, phi: float) -> object:
        if not isinstance(rho, int | float) or not isinstance(phi, int | float):
            raise TypeError("Both arguments should be floats or integers")
        if rho < 0:
            raise ValueError("The modulus of the vector should be positive")
        return Vec2(rho * math.cos(phi), rho * math.sin(phi))

    @staticmethod
    def cross_prod_module(a: object, b: object) -> float:
        if not isinstance(a, Vec2) or not isinstance(b, Vec2):
            raise TypeError("Both arguments should be Vec2")
        return a.module * b.module * math.sin(Vec2.get_angle_between(a, b))

    @staticmethod
    def are_orthogonal(a: object, b: object) -> bool:
        if not isinstance(a, Vec2) or not isinstance(b, Vec2):
            raise TypeError("Both arguments should be Vec2")
        return bool(a * b)

    # ! this function returns the angle of b-a not a-b
    @staticmethod
    def get_angle_between(a: object, b: object) -> float:
        return b.phase - a.phase
