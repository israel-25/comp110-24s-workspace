"""Test my garden functions."""

__author__ = "730470758"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
"""Importing functions from garden_helpers.py"""


def test_add_by_kind() -> None:
    """Test add_by_kind function."""
    dictionary = {}
    add_by_kind(dictionary, "Flower", "Rose")
    assert dictionary == {"Flower": ["Rose"]}


def test_add_by_kind_empty() -> None:
    """Test add_by_kind function."""
    empty_plant_name_dictionary = {}
    add_by_kind(empty_plant_name_dictionary, "Flower", "")
    assert empty_plant_name_dictionary == {"Flower": [""]}


def test_add_by_date() -> None:
    """Test add_by_date function."""
    dictionary = {"2024-01-01": ["Tulip"]}
    add_by_date(dictionary, "2024-01-01", "Rose")
    assert dictionary == {"2024-01-01": ["Tulip", "Rose"]}


def test_add_by_date_newdate() -> None:
    """Test add_by_date function."""
    dictionary = {}
    add_by_date(dictionary, "2024-01-01", "Lily")
    assert dictionary == {"2024-01-01": ["Lily"]}


def test_lookup_by_kind_and_date() -> None:
    """Test lookup_by_kind_and_date function."""
    Kind = {"Flower": ["Rose", "Daisy"], "Tree": ["Oak", "Pine"]}
    Date = {"2024-01-01": ["Rose", "Daisy", "Tulip"], "2024-02-01": ["Oak", "Pine"]}
    assert lookup_by_kind_and_date(Kind, Date, "Flower", "2024-01-01") == "Flowers to plant in 2024-01-01"


def test_lookup_by_kind_and_date_noplants() -> None:
    """Test lookup_by_kind_and_date function."""
    Kind = {"Flower": ["Rose", "Lily"], "Tree": ["Oak", "Pine"]}
    Date = {"2024-01-01": ["Oak", "Pine"], "2024-02-01": ["Daisy", "Sunflower"]}
    assert lookup_by_kind_and_date(Kind, Date, "Flower", "2024-01-01") == "No Flowers to plant in 2024-01-01."