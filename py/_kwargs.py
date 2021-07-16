# ** kwargs =   parameter that will pack all argument into a dictionary useful so that a function can
#               accept a varying amount of keyword argument

def hello(**kwargs):
    # print("hello " + kwargs['first'] + " " + kwargs['last'])
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Bro", middle="Dub", last="Code")
