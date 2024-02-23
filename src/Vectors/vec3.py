import math
from typing import List, Tuple

from .vec2 import Vec2
from .vecn import Vector


class Vec3(Vector):
    def __init__(self, *coords: Tuple[float]) -> None:
        if len(coords) != 3:
            raise TypeError(
                f"Vector objects must have 2 argument, {len(coords)} where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: List[float] = list(coords)

    @property
    def x(self) -> float:
        return self.coords[0]

    @property
    def y(self) -> float:
        return self.coords[1]

    @property
    def z(self) -> float:
        return self.coords[2]

    @property
    def polar(self) -> float:
        if self.is_zero():
            raise ValueError("The polar angle of a zero vector it's undefined")
        if self.z == 0:
            return math.pi / 2
        return (
            math.atan(Vec2(self.x, self.y).module / self.z)
            + math.pi / 2
            + math.copysign(math.pi / 2, self.z)
        )

    @property
    def azimuth(self) -> float:
        if self.x == 0 and self.y == 0:
            raise ValueError("The azimuth of a vector with x=0 and y=0 it's undefined")
        if self.x == 0:
            return math.copysign(math.pi, self.y)
        return math.tan(self.y / self.x) + (
            0 if self.x > 0 else math.copysign(math.pi, self.y)
        )

    @property
    def radial_dist(self) -> float:
        return Vec2(self.x, self.y).module

    def get_phases(self) -> Tuple[float]:
        return self.polar, self.azimuth

    def get_spherical_coordinates(self) -> Tuple[float]:
        return self.module, *self.get_phases()

    def get_cylindrical_coordinates(self) -> Tuple[float]:
        return self.radial_dist, self.azimuth, self.z

    @classmethod
    def from_spherical(cls, rho: float, polar: float, azimuth: float) -> object:
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
