# filter(function, iterable)


friends = [
    ("Rachel", 18),
    ("Joey", 20),
    ("David", 16),
    ("Rose", 21)
]

age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)


#
result = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])
print(list(result))
