"""File to define River class."""

__author__ = "730470758"
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Class that creates a river object with 3 attributes."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Method that checks the method of fish and bears in the river."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears

    def bears_eating(self):
        """Method that simulates the act of a bear eating fish in the river.""" 
        for elem in self.bears:
            if len(self.fish) >= 5:
                elem.eat(3)
                self.remove_fish(3)
            elif len(self.fish) < 5 and len(self.fish) > 0:
                elem.one_day()
        return None
    
    def check_hunger(self):
        """Method used to check the hunger score of bears in the river."""
        for i in self.bears:
            j: int = 0
            if i.hunger_score < 0:
                self.bears.pop(j)
            j += 1
        return None

    def repopulate_fish(self) -> None:
        """Method used to repopulate the river with fish based on amount in river."""
        fish_count: int = len(self.fish)
        if fish_count >= 2:
            for x in range(0, fish_count // 2):
                for i in range(4):
                    self.fish.append(Fish())
        return None
    
    def repopulate_bears(self) -> None:
        """Method used to repopulate bears in river."""
        bear_count: int = len(self.bears)
        for i in range(bear_count // 2):
            new_bear: Bear = Bear()
            self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """Method that shows the number of fish and bears in river each day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None:
        """Method that shows the total number of bears and fish in the river each day for a week."""
        for i in range(1, 8):
            self.one_river_day()
    
    def remove_fish(self, amount: int) -> None:
        """Method used to remove fish from river."""
        for i in range(amount):
            self.fish.pop(0)