import math
from typing import Tuple

from .vecn import Vector


class Vec3(Vector):
    """class for 3-dimensional vectors (right-handed).

    subclass of Vector
    """

    def __init__(self, *coords: float) -> None:
        """Create an object from an unpacked tuple of 3 coordinates"""
        if len(coords) != 3:
            raise TypeError(
                f"Vector objects must have 2 argument, {len(coords)} where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: Tuple[float] = tuple(coords)

    @property
    def x(self) -> float:
        """return the x (first) coordinate of the vector"""
        return self.coords[0]

    @property
    def y(self) -> float:
        """return the y (second) coordinate of the vector"""
        return self.coords[1]

    @property
    def z(self) -> float:
        """return the z (third) coordinate of the vector"""
        return self.coords[2]

    @property
    def polar(self) -> float:
        """return the polar angle in spherical coordinates (angle from the z-axis)"""
        if self.is_zero():
            raise ValueError("The polar angle of a zero vector it's undefined")
        if self.z == 0:
            return math.pi / 2
        return (
            math.atan(Vector(self.x, self.y).module / self.z)
            + math.pi / 2
            + math.copysign(math.pi / 2, self.z)
        )

    @property
    def azimuth(self) -> float:
        """return the azimuthal angle in spherical coordinates (angle from the x-axis)"""
        if self.x == 0 and self.y == 0:
            raise ValueError("The azimuth of a vector with x=0 and y=0 it's undefined")
        if self.x == 0:
            return math.copysign(math.pi, self.y)
        return math.tan(self.y / self.x) + (
            0 if self.x > 0 else math.copysign(math.pi, self.y)
        )

    @property
    def radial_dist(self) -> float:
        """return the radial distance in cylindrical coordinates"""
        return Vector(self.x, self.y).module

    def get_phases(self) -> Tuple[float]:
        """return polar and azimuthal angles"""
        return self.polar, self.azimuth

    def get_spherical_coordinates(self) -> Tuple[float]:
        """return spherical coordinates"""
        return self.module, *self.get_phases()

    def get_cylindrical_coordinates(self) -> Tuple[float]:
        """return cylindrical coordinates"""
        return self.radial_dist, self.azimuth, self.z

    def __radd__(self, other):
        """definition of reverse addition"""
        return self + other

    def __rsub__(self, other):
        """definition of reverse addition"""
        return -self + other

    # TODO
    def __matmul__(self, other: object) -> object:
        """definition of cross product"""
        pass

    # TODO
    def rotate_x(self, phi: float) -> None:
        """In place counter clockwise rotation around the x-axis"""
        pass

    # TODO
    def rotate_y(self, phi: float) -> None:
        """In place counter clockwise rotation around the y-axis"""
        pass

    # TODO
    def rotate_z(self, phi: float) -> None:
        """In place counter clockwise rotation around the z-axis"""
        pass

    @classmethod
    def from_spherical(cls, rho: float, polar: float, azimuth: float) -> object:
        """Create a Vec3 from spherical coordinates"""
        if (
            not isinstance(rho, int | float)
            or not isinstance(polar, int | float)
            or not isinstance(azimuth, int | float)
        ):
            raise TypeError("All three arguments should be floats or integers")
        if rho < 0:
            raise ValueError("The modulus of the vector should be positive or zero")
        return Vec3(
            rho * math.sin(polar) * math.cos(azimuth),
            rho * math.sin(polar) * math.sin(azimuth),
            rho * math.cos(polar),
        )

    @classmethod
    def from_cylindrical(cls, radial_dist: float, azimuth: float, z: float) -> float:
        """Create a Vec3 from cylindrical coordinates"""
        if (
            not isinstance(radial_dist, int | float)
            or not isinstance(azimuth, int | float)
            or not isinstance(z, int | float)
        ):
            raise TypeError("All three arguments should be floats or integers")
        if radial_dist < 0:
            raise ValueError(
                "The modulus of the radial distance should be positive or zero"
            )
        return Vec3(radial_dist * math.cos(azimuth), radial_dist * math.sin(azimuth), z)
