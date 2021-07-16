def show():
    for i in range(1, 11):
        print(i, end=" ")
    print()


def sum_lst(lst):
    sum2 = 0
    for i in lst:
        if i % 2 == 0:
            sum2 += i
    return sum2


#
def count_char(s):
    count_upper = 0
    count_lower = 0
    for i in s:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1
    return "lower: " + str(count_lower) + "\n" + "upper: " + str(count_upper)


# 2,2,3,4 -> 2,3,4
def get_unique_values(list1):
    ans = []
    for i in list1:
        if i not in ans:
            ans.append(i)
    return ans


# SNT
def get_snt(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
