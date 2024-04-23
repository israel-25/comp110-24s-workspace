"""Splitting a dictionary into two lists."""

__author__ = "730470758"


def get_keys(keys: dict[str, int]) -> list[str]:
    """Get Keys."""
    key_list: list[str] = []
    if not keys:
        return key_list
    else:
        for key in keys:
            key_list.append(key)
        return key_list
    

def get_values(value: dict[str, int]) -> list[int]:
    """Get Values."""
    value_list: list[int] = []
    if not value:
        return value_list
    else:
        for val in value.values():
            value_list.append(val)
        return value_list