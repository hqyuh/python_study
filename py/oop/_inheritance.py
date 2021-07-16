# kế thừa

class Animal:
    alive = True

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Rabbit(Animal):
    pass


class Fish(Animal):
    def swim(self):
        print("The fish is swimming")


class Hawk(Animal):
    pass


fish = Fish()
print(fish.alive)
fish.eat()
fish.swim()


