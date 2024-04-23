"""Functions that implement sorting algorithms."""

__author__ = "730470758"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm."""
    n = len(x)  
    for i in range(1, n):
        current_element = x[i] 
        j = i - 1  
        while j >= 0 and x[j] > current_element:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = current_element
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm."""
    for i in range(len(x)):
        min_index = i 
        for j in range(i + 1, len(x)):
            if x[j] < x[min_index]:
                min_index = j
        if min_index != i:
            x[i], x[min_index] = x[min_index], x[i]
    return None
    