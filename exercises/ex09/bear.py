"""File to define Bear class."""


class Bear:
    """Class that creates bear object with two attributes."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initializing bear object."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Adjusting hunger score and age of bear as one day passes."""
        self.hunger_score -= 1
        self.age += 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Updating bears hunger score based on the number of fish it had eaten."""
        self.hunger_score += num_fish