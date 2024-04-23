"""Summing the elements of a list using different loops."""

__author__ = "730470758"


def w_sum(vals: list[float]) -> float:
    """While Loop function."""
    counter: int = 0
    totalsum: float = 0
    while counter < len(vals):
        totalsum += vals[counter]
        counter += 1
    return totalsum


def f_sum(vals: list[float]) -> float:
    """For loop without range."""
    totalsum: float = 0
    for elem in vals:
        totalsum += elem
    return totalsum


def f_range_sum(vals: list[float]) -> float:
    """For loop with range."""
    totalsum: float = 0
    for elem in range(0, len(vals)):
        totalsum += vals[elem]
    return totalsum
