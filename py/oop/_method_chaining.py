# method chaining = calling multiple method sequentially each call
#                   performs an action on same object and return self


class Car:

    # phải return chứ không là NoneType
    def turn_on(self):
        print("You start")
        return self

    def drive(self):
        print("You drive")
        return self

    def turn_off(self):
        print("You stop")
        return self


car = Car()

car.turn_on()\
    .drive()
