from abc import ABC, abstractmethod

# This page manages the abstraction of classes.
class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Fido")
cat = Cat("Garfield")

print(dog.speak())
print(cat.speak())
