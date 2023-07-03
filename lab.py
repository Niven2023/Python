from abc import ABC, abstractmethod


class AbstractAnimalHome(ABC):
    def __init__(self, name, location, area):
        self.name = name
        self.location = location
        self.area = area

    @abstractmethod
    def calculate_cost_per_month(self):
        pass


class Zoo(AbstractAnimalHome):
    def __init__(self, name, location, area, capacity, working_hours, daily_cost):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.working_hours = working_hours
        self.daily_cost = daily_cost

    def calculate_cost_per_month(self):
        return self.daily_cost * 30


class Farm(AbstractAnimalHome):
    def __init__(self, name, location, area, animal_type, daily_food_cost):
        super().__init__(name, location, area)
        self.animal_type = animal_type
        self.daily_food_cost = daily_food_cost

    def calculate_cost_per_month(self):
        return self.daily_food_cost * 30


class AnimalHomeManager:
    def __init__(self):
        self.animal_homes = []

    def add_animal_home(self, animal_home):
        self.animal_homes.append(animal_home)

    def print_animal_homes(self):
        for animal_home in self.animal_homes:
            print(animal_home)


zoo = Zoo("Kyiv Zoo", "Kyiv", 92, 3292, "9:00 - 18:00", 5000)
farm1 = Farm("Cattle Farm", "Rural Area", 500, "Cattle", 1000)
farm2 = Farm("Poultry Farm", "Rural Area", 300, "Poultry", 500)

animal_home_manager = AnimalHomeManager()
animal_home_manager.add_animal_home(zoo)
animal_home_manager.add_animal_home(farm1)
animal_home_manager.add_animal_home(farm2)

animal_home_manager.print_animal_homes()
