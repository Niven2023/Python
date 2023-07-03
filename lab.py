class Zoo:
    def __init__(self, name=None, location=None, area=0.0, capacity=0):
        self.name = name
        self.location = location
        self.area = area
        self.capacity = capacity

    @staticmethod
    def get_instance():
        return Zoo.instance

    def increase_capacity(self, count):
        self.capacity += count

    def split_area(self):
        self.area /= 2

    def add_new_region(self, area):
        self.area += area

    def __str__(self):
        return f"Zoo(name={self.name}, location={self.location}, area={self.area}, capacity={self.capacity})"


Zoo.instance = Zoo()

if __name__ == "__main__":
    ZooArray = [None] * 4
    ZooArray[0] = Zoo()
    ZooArray[1] = Zoo("Kyiv Zoo", "Kyiv", 92, 3292)
    ZooArray[2] = Zoo.get_instance()
    ZooArray[3] = Zoo.get_instance()
    print(ZooArray[1])
