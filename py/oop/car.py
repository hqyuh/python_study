
class Car:

    # attribute
    # make = None

    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make   # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + "is driving")

    def stop(self):
        print("This " + self.model + "is car is stopped")
