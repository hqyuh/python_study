# sort() method   = used with lists
# sort() function = used with iterables

# list

# students = ["Q", "A", "E", "R"]
# students.sort()  # reverse=True
#
# for i in students:
#     print(i, end=" ")

print("")
# tuples

# students1 = ("Q", "A", "E", "R")
# sorted_students = sorted(students1, reverse=True)
# for i in sorted_students:
#     print(i, end=" ")


students = [
    ("James", "F", 20),
    ("Sandy", "A", 40),
    ("Patrick", "D", 10),
]

age = lambda x: x[2]
students.sort(key=age)

for i in students:
    print(i)
