# kế thừa đa cấp

class Organism:

    alive = True


class Animal(Organism):

    def eat(self):
        print("eating")


class Dog(Animal):
    def bark(self):
        print("barking")


dog = Dog()
print(dog.alive)
dog.eat()
