"""File to define Fish class."""


class Fish:
    """Fish class that creates object with one attribute."""
    age: int
    
    def __init__(self):
        """Initializing the age for a fish object."""
        self.age = 0
        return None
    
    def one_day(self):
        """Adjusting age for fish object as each day passes."""
        self.age += 1
        return None