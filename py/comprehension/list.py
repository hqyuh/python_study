

# list = [expression for item in iterable]


# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

# squares = [i * i for i in range(1, 11)]
# print(squares)


##

student = [100, 90, 80, 70]
# passed_student = list(filter(lambda x: x >= 90, student))
# passed_student = [i for i in student if i >= 90]
passed_student = [i if i >= 90 else "FAILED" for i in student]
print(passed_student)




