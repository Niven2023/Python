class AbstractAnimalHome(ABC):
    def __init__(self, name, location, area):
        self.name = name
        self.location = location
        self.area = area

    @abstractmethod
    def calculate_cost_per_month(self):
        pass

    def do_something(self):
        pass


class Zoo(AbstractAnimalHome):
    def __init__(self, name, location, area, capacity, working_hours, daily_cost):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.working_hours = working_hours
        self.daily_cost = daily_cost

    def calculate_cost_per_month(self):
        return self.daily_cost * 30

    def do_something(self):
        return "Zoo"


class Farm(AbstractAnimalHome):
    def __init__(self, name, location, area, animal_type, daily_food_cost):
        super().__init__(name, location, area)
        self.animal_type = animal_type
        self.daily_food_cost = daily_food_cost

    def calculate_cost_per_month(self):
        return self.daily_food_cost * 30

    def do_something(self):
        return "Farm"


class InvalidAnimalException(Exception):
    pass


class AnimalHomeManager:
    def __init__(self):
        self.animal_homes = []

    def add_animal_home(self, animal_home):
        if not isinstance(animal_home, (Zoo, Farm)):
            raise InvalidAnimalException("Invalid animal type")
        self.animal_homes.append(animal_home)

    def __len__(self):
        return len(self.animal_homes)

    def __getitem__(self, index):
        return self.animal_homes[index]

    def __iter__(self):
        return iter(self.animal_homes)

    def calculate_do_something_results(self):
        return [animal_home.do_something() for animal_home in self.animal_homes]

    def get_concatenated_objects_with_indices(self):
        return [(index, str(animal_home)) for index, animal_home in enumerate(self.animal_homes)]

    def get_objects_with_do_something_results(self):
        return [(animal_home, animal_home.do_something()) for animal_home in self.animal_homes]

    def get_attribute_values_by_type(self, data_type):
        return {key: value for key, value in self.animal_homes[0].__dict__.items()
                if isinstance(value, data_type)}

    def check_condition_for_all_objects(self, condition):
        return {'all': all(condition(animal_home) for animal_home in self.animal_homes)}

    def check_condition_for_any_object(self, condition):
        return {'any': any(condition(animal_home) for animal_home in self.animal_homes)}


import logging

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(str(e))
                elif mode == "file":
                    logging.basicConfig(filename="logfile.log", level=logging.ERROR)
                    logging.error(str(e))
                else:
                    raise ValueError("Invalid logging mode")
        return wrapper
    return decorator


zoo = Zoo("Kyiv Zoo", "Kyiv", 92, 3292, "9:00 - 18:00", 5000)
farm1 = Farm("Cattle Farm", "Rural Area", 500, "Cattle", 1000)
farm2 = Farm("Poultry Farm", "Rural Area", 300, "Poultry", 500)

animal_home_manager = AnimalHomeManager()
animal_home_manager.add_animal_home(zoo)
animal_home_manager.add_animal_home(farm1)
animal_home_manager.add_animal_home(farm2)

@logged(InvalidAnimalException, "console")
def example_function():
    animal_home_manager.add_animal_home("Invalid Animal")

example_function()

print("Calculate do_something results:", animal_home_manager.calculate_do_something_results())
print("Concatenated objects with indices:", animal_home_manager.get_concatenated_objects_with_indices())
print("Objects with do_something results:", animal_home_manager.get_objects_with_do_something_results())
print("Attribute values of type int:", animal_home_manager.get_attribute_values_by_type(int))
print("Condition for all objects:", animal_home_manager.check_condition_for_all_objects(
    lambda animal_home: animal_home.area > 100))
print("Condition for any object:", animal_home_manager.check_condition_for_any_object(
    lambda animal_home: animal_home.location == "Rural Area"))
