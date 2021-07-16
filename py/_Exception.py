
try:
    a = int(input("a? "))
    b = int(input("b? "))
    result = a / b
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! ")
except ValueError as e:
    print(e)
    print("Enter only number")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("this will always execute")
