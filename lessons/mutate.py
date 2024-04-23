"""Mutating functions."""

__author__ = "730470758"


def manual_append(a: list[int], num: int) -> None:  
    """Manual append function."""
    a.append(num)


def double(a: list[int]) -> None:
    """Double function."""
    counter: int = 0
    while counter < 3:
        a[counter] = a[counter] * 2
        counter += 1