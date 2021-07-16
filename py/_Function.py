def hello(name, age, address):
    print(name + " " + str(age) + " " + address)


hello(name="Huy", address='DN', age=20)


def multiply(a, b):
    return a * b


print(multiply(6, 8))


#
q = "Bro"  # global scope


def display_name():
    name = "Code"  # local scope
    print(name)


display_name()
print(q)
