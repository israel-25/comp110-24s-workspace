"""Recursion !!!"""
 
__author__ = "730470758"


def f(n: int, b: int) -> int:
    """Recursion function."""
    if n == 0 or b == 0:
        return 0
    elif n == 1:
        return b
    elif b == 1:
        return n
    else:
        return n + f(n, b - 1)