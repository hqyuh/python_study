# ghi đè


class Animal:

    def eat(self):
        print("This animal")


class Rabbit(Animal):

    def eat(self):
        print("This rabbit")


rabbit = Rabbit()
rabbit.eat()
