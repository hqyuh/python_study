# *args =   parameter that will pack all arguments into a tuple useful so that a function
#           can accept a varying amount of arguments

def add(*args):
    sum2 = 0
    # args = list(args)
    # args[0] = 0
    for i in args:
        sum2 += i
    return sum2


print(add(1, 2, 3, 4, 5, 6))

