vowel = ['a', 'e', 'i', 'u']
list1 = [4, 5, 3, 7, 6, 1]

vowel.insert(3, 'H')
vowel.remove('a')
vowel.pop(0)
print(vowel)

# sort
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#
vowel.reverse()
print("reverse: ", vowel)


#
list2 = [15, 5, 20, 3, 7]
new_arr = []
for i in list2:
    if i % 5 == 0:
        new_arr.append(i)
if len(new_arr) == 0:
    new_arr = [0]
print(new_arr)


