import math
from typing import Tuple

from .vecn import Vector


class Vec2(Vector):
    """class for 2-dimensional vectors.

    subclass of Vector
    """

    def __init__(self, *coords: float) -> None:
        """Create an object from an unpacked tuple of 2 coordinates"""
        if len(coords) != 2:
            raise TypeError(
                f"Vector objects must have 2 argument, {len(coords)} where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: tuple[float] = tuple(coords)

    @property
    def x(self) -> float:
        """return the x (first) coordinate of the vector"""
        return self.coords[0]

    @property
    def y(self) -> float:
        """return the y (second) coordinate of the vector"""
        return self.coords[1]

    @property
    def phase(self) -> float:
        """return the angle between the x-axis and the vector"""
        if self.is_zero():
            raise ValueError("The phase of a zero vector it's undefined")
        if self.x == 0:
            return math.copysign(math.pi, self.y)
        return math.tan(self.y / self.x) + (
            0 if self.x > 0 else math.copysign(math.pi, self.y)
        )

    def __radd__(self, other):
        """definition of reverse addition"""
        return self + other

    def __rsub__(self, other):
        """definition of reverse addition"""
        return -self + other

    # TODO
    # ? should I add this?
    def __complex__():
        """return a complex number from a Vec2"""
        pass

    def get_polar_coord(self) -> Tuple[float]:
        """return the polar coordinates of the vector"""
        return self.module, self.phase

    def project_tangent(self, other: object) -> object:
        """get the tangent vector projection of other on self

        Args:
            other (object): Vec2

        Returns:
            object: a vector with the same direction as self and module equal to
                other * cos(angle in between)
        """
        if not isinstance(other, Vec2):
            raise TypeError("To make a projection both vectors must be Vec2D")
        return (
            self.get_normalized()
            * other.module
            * math.cos(Vec2.get_angle_between(self, other))
        )

    def project_normal(self, other: object) -> object:
        """Get the normal vector projection of other on self

        Args:
            other (object): Vec2

        Returns:
            object: a vector perpendicular to self and module equal to
                other * sin(angle in between), also equal to
                other - self.project_tangent(other)
        """
        if not isinstance(other, Vec2):
            raise TypeError("To make a projection both vectors must be Vec2D")
        return other - self.project_tangent(other)

    def project_components(self, other: object) -> Tuple[object]:
        """get both projection of other on self

        Args:
            other (object): Vec2

        Returns:
            Tuple[object]: Two Vec2
                the first is the Tangent component and the second is the normal
        """
        return self.project_tangent(other), self.project_normal(other)

    @classmethod
    def from_complex(cls, num: complex) -> object:
        """Create a Vec2 from a complex number, x=Re and y=Im"""
        if not isinstance(num, complex):
            raise TypeError("Argument should be a complex number")
        return Vec2(num.real, num.imag)

    @classmethod
    def from_polar(cls, rho: float, phi: float) -> object:
        """Create a Vec2 from polar coordinates"""
        if not isinstance(rho, int | float) or not isinstance(phi, int | float):
            raise TypeError("Both arguments should be floats or integers")
        if rho < 0:
            raise ValueError("The modulus of the vector should be positive")
        return Vec2(rho * math.cos(phi), rho * math.sin(phi))

    @staticmethod
    def cross_prod_module(a: object, b: object) -> float:
        """Get the module of the cross product of two Vec2"""
        if not isinstance(a, Vec2) or not isinstance(b, Vec2):
            raise TypeError("Both arguments should be Vec2")
        return a.module * b.module * math.sin(Vec2.get_angle_between(a, b))

    # ! this function returns the angle of b-a not a-b
    @staticmethod
    def get_angle_between(a: object, b: object) -> float:
        """return the angle between two vectors, note its second Vec2 - first Vec2"""
        return b.phase - a.phase
