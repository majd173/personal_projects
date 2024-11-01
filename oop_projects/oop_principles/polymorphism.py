# This page manages inheritance and polymorphism.
class Vehicle:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def drive(self):
        return f'{self.name} {self.model} is driving'


class Car(Vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color

    def drive(self):
        return f'{self.name} {self.model} is driving in {self.color}'


class Truck(Vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color

    def drive(self):
        return f'{self.name} {self.model} is driving in {self.color}'


car_1 = Car('Toyota', 'Corolla', 'blue')
print(car_1.drive())

truck_1 = Truck('Ford', 'F150', 'red')
print(truck_1.drive())
