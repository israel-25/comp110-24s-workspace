"""File to define River class"""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
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
        if len(self.fish) >= 5: 
            for i in range(0,2):
                self.fish.pop(i)
        return None
    
    def check_hunger(self):
        for i in self.bears[i]:
            j: int = 0
            if self.bears[i].hunger_score <0:
                self.bears[i].pop(j)
            j+=1
        return None
        
    def repopulate_fish(self):
        if len(self.fish) >= 2:
            self.fish = (len(self.fish) * 4)
        return None
    
    def repopulate_bears(self):
        if len(self.bears) >= 2:
            self.bears = (len(self.bears) // 2) + self.bears
        return None
    
    def view_river(self):
        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        i: int = 0
        while i < 7:
            self.one_river_day
            i += 1
    

    def remove_fish(self,amount:int) -> None:
        for i in range(0,amount):
            self.fish.pop(i)

