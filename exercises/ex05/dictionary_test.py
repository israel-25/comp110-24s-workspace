"""Dictionary Test program!"""

__author__ = "730470758"

import pytest
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

dictionary: dict[str] = {"Israel": "blue", "Kyle": "blue", "Charlie": "red", "Josh": "blue", "Michael": "green"}


def test_invert_usecase():
    """Testing invert function with a use case."""
    dictionary = {
        "Israel": "blue",
        "Kyle": "green",
        "Charlie": "red",
        "Josh": "yellow",
        "Michael": "purple"
    }
    inverted = invert(dictionary)
    assert inverted == {
        "blue": "Israel",
        "green": "Kyle",
        "red": "Charlie",
        "yellow": "Josh",
        "purple": "Michael"
    }


def test_invert_edgecase():
    """Testing invert function with an edge case."""
    with pytest.raises(KeyError):
        invert({
            "Israel": "blue",
            "Kyle": "blue"
        })


def test_invert_edgecase2():
    """Testing invert function to see behavior to empty dictionary."""
    inverted = invert({})
    assert inverted == {}


def test_favorite_color_usecase():
    """Testing favorite color function with use case."""
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_edgecase():
    """Testing favorite color function to see how it reacts to empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_edgecase2():
    """Testing favorite color function with edge case."""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_count_usecase():
    """Testing count function with use case."""
    result = count(["a", "b", "a", "c", "b", "a"])
    assert result == {"a": 3, "b": 2, "c": 1}


def test_count_edgecase():
    """Testing count function to see how it reacts to an empty dictionary as input."""
    result = count([])
    assert result == {}


def test_count_extra_edgecase():
    """Testing count function that has input with repeating elements."""
    # Test for a list with repeated elements
    result = count(["a", "a", "a"])
    assert result == {"a": 3}


def test_alphabetizer_usecase():
    """Testing alphabetizer with use case."""
    result = alphabetizer(["apple", "banana", "carrot", "avocado"])
    assert result == {
        "a": ["apple", "avocado"],
        "b": ["banana"],
        "c": ["carrot"]
    }


def test_alphabetizer_edgecase():
    """Testing to see the behavior of alphabetizer with an empty dictionary."""
    result = alphabetizer([])
    assert result == {}


def test_alphabetizer_edgecase2():
    """Testing alphabetizer when a list of non alphabetic characters are input."""
    result = alphabetizer(["123", "abc", "456"])
    assert result == {"a": ["abc"]} 


def test_update_attendance_usecase():
    """Testing update attendance function with a use case."""
    attendance = {"Monday": ["Israel", "Kyle"], "Tuesday": ["Michael"]}
    update_attendance(attendance, "Monday", "David")
    assert attendance == {"Monday": ["Israel", "Kyle", "David"], "Tuesday": ["Michael"]}


def test_update_attendance_edgecase():
    """Testing update attendance function with an edge case."""
    attendance = {}
    update_attendance(attendance, "Monday", "Israel")
    assert attendance == {"Monday": ["Israel"]}


def test_update_attendance_edgecase2():
    """Testing update attendance function that updates attendance with a new day."""
    # Test for updating attendance with a new day
    attendance = {"Friday": ["Israel", "Kyle"]}
    update_attendance(attendance, "Thursday", "Michael")
    assert attendance == {"Friday": ["Israel", "Kyle"], "Thursday": ["Michael"]}