
# min
list1 = [2, 4, 5, 6]
min1 = list1[0]
for i in list1:
    if i < min1:
        min1 = i
print("min = ", min1)


# n = 3
# list2 = []
# for i in range(n):
#     list2.append(int(input()))
# min2 = list2[0]
# for i in list2:
#     if i < min2:
#         min2 = i
# print("min = ", min2)


# sort
list3 = [3, 6, 0, 4]
# for i in range(len(list3)):
#     print(list3[i])
for i in range(len(list3)):
    for j in range(i):
        if list3[i] < list3[j]:
            temp = list3[i]
            list3[i] = list3[j]
            list3[j] = temp
print(list3)
