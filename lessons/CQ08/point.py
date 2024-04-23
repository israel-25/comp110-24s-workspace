"""CQ08 !!!"""
from __future__ import annotations
__author__ = "730470758"


class Point:
    """Creating a class called point with an x and y as attributes."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """Create a new point object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating point by scaling by a given factor."""
        self.x = self.x * factor
        self.y = self.y * factor
    
    def scale(self, factor: int) -> Point:
        """Creating new point from values of given point without mutating original point."""
        new_point: Point
        new_point = Point(self.x * factor, self.y * factor)
        return new_point