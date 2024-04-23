"""Dictionary program!"""

__author__ = "730470758"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting Dictionary."""
    new_dictionary: dict[str, str] = {}
    for key, value in dictionary.items():
        if value in new_dictionary:
            raise KeyError("Duplicate value encountered while inverting the dictionary.")
        new_dictionary[value] = key
    return new_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """Searching through dictionary to find most liked color."""
    color_count: dict[str, int] = {}
    if not dictionary:  # Check if dictionary is empty
        return ""
    color_count: dict[str, int] = {}
    for color in dictionary.values():
        color_count[color] = color_count.get(color, 0) + 1
    most_common_color = max(color_count, key=lambda k: color_count[k])
    return most_common_color


def count(val: list[str]) -> dict[str, int]:
    """Count function."""
    result: dict[str, int] = {}
    for key in val:
        result[key] = result.get(key, 0) + 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group variables by the first letter in their name."""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter.isalpha():
            result.setdefault(first_letter, []).append(word)
    return result


def update_attendance(dictionary: dict[str, list[str]], day: str, student: str) -> None:
    """Function to update."""
    if day not in dictionary:
        dictionary[day] = [student]
    elif student not in dictionary[day]:
        dictionary[day].append(student)
