# This page manages inheritance.
class Vehicle:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def drive(self):
        return f"{self.name} {self.model} is driving"


class Toyota(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)


car_1 = Toyota("Toyota", "Corolla")
print(car_1.drive())
