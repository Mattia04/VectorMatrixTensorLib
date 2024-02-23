import math
from typing import List, Tuple

from .vecn import Vector


class Vec2(Vector):
    def __init__(self, *coords: Tuple[float]) -> None:
        if len(coords) != 3:
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
    def z(self):
        return self.coords[2]

    @property
    def polar(self):
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
    def azimuth(self):
        if self.x == 0 and self.y == 0:
            raise ValueError("The azimuth of a vector with x=0 and y=0 it's undefined")
        if self.x == 0:
            return math.copysign(math.pi, self.y)
        return math.tan(self.y / self.x) + (
            0 if self.x > 0 else math.copysign(math.pi, self.y)
        )

    @property
    def phases(self):
        return self.polar, self.azimuth
