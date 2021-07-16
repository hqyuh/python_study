
# map(function, iterable)

# store = [
#     ("shirt", 20.00),
#     ("pants", 10.00),
#     ("socks", 40.00)
# ]
#
# to_dollars = lambda data: (data[0], data[1] / 0.82)
# store_dollars = list(map(to_dollars, store))
#
# for i in store_dollars:
#     print(i)


#
numbers = (5, 10, 15)
result = map(lambda x: x*x, numbers)
print(t := list(result))

#
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))
