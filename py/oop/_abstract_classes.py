# abstract

# https://toidicode.com/abstraction-trong-python-362.html

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print("Car go")


car = Car()
car.go()


