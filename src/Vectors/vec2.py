import cmath
from typing import List, Tuple

import Vectors.vecn as vecn


class Vec2(vecn.Vector):
    def __init__(self, *coords: Tuple[float]) -> None:
        if len(coords) != 2:
            raise TypeError(
                f"Vector objects must have 2 argument, {len(coords)} where given"
            )
        if any(not isinstance(coord, int | float) for coord in coords):
            raise TypeError("Vector arguments must be int or float")

        self.coords: List[float] = list(coords)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -self + other

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def phase(self) -> float:
        return cmath.phase(complex(self.x, self.y))

    def get_polar_coord(self) -> Tuple[float]:
        return self.module, self.phase
