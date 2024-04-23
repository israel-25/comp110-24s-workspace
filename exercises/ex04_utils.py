"""List Utility Functions!"""

__author__ = "730470758"


def all(list: list[int], int1: int) -> bool:
    """All function."""
    counter: int = 0
    True_false: bool
    if len(list) == 0:
        return False
    while counter < len(list):
        if int1 == list[counter]:
            counter += 1
        True_false = True
        if int1 != list[counter]:
            True_false = False
            counter += 1
        return True_false
    return True_false


def max(list: list[int]) -> int:
    """Max function."""
    if len(list) == 0:
        raise ValueError(" max() arg is an empty List")
    else:
        counter: int = 0
        max = list[counter]
        while counter < len(list):
            if list[counter] > max:
                max = list[counter]
            counter += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Is equal to function."""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
    

def extend(list1: list[int], list2: list[int]) -> None:
    """Extend function."""
    counter: int = 0
    while counter < len(list2):
        list1.append(list2[counter])
        counter += 1
