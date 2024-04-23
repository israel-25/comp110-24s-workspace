"""Some functions for my garden plan!"""
__author__ = "730470758"


def add_by_kind(Dictionary: dict[str, list[str]], Kind: str, plant: str) -> None:
    """Add elements to the Dictionary given by kind."""
    if Kind in Dictionary:
        Dictionary[Kind].append(plant)
    else: 
        Dictionary[Kind] = []
        Dictionary[Kind].append(plant)


def add_by_date(Dictionary: dict[str, list[str]], Date: str, plant: str) -> None:
    """Add elements to the Dictionary given by date."""
    if Date in Dictionary:
        Dictionary[Date].append(plant)
    else: 
        Dictionary[Date] = []
        Dictionary[Date].append(plant)


def lookup_by_kind_and_date(Kind: dict[str, list[str]], Date: dict[str, list[str]], by_kind: str, by_date: str) -> str:
    """Add elements to the Dictionary given by kind and date."""
    assert by_kind in Kind
    assert by_date in Date
    """Get a list of all plants of the specific kind input""" 
    kind_list: list[str] = Kind[by_kind]
    """ Get a list of all plants planted in a specific month"""
    month_list: list[str] = Date[by_date]
    """Go through both lists and find elements that appear in both."""
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:
                combined_list.append(other_plant)
    
    if len(combined_list) > 0:
        return f"{by_kind}s to plant in {by_date}"
    else:
        return f"No {by_kind}s to plant in {by_date}."