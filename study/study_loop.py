
# while
i = 1
while i < 6:
    print(i, end=' ')
    i += 1

print('')
# lambda
my_list = [5, 2, 6, 4, 1, 9, 7]
result = list(filter(lambda x: x % 2 == 0, my_list))
print(result)


my_list1 = [1, 5, 4, 6, 8, 11, 3, 12]
result1 = list(map(lambda x: x * 2, my_list1))
print(result1)

#
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result2 = list(map(lambda x, y: x + y, num1, num2))
print(result2)
