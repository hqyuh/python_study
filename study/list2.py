

list1 = ['a', 'b', 'c']
list2 = ['d', 'e']

# add
list2.insert(2, 'f')
list1.extend(list2)

print(list1[0:1])

#
this_tuple = ('h', 'j')
list2.extend(this_tuple)
print(list2)


# remove
list2.remove('j')
list2.pop(1)
# del last
list2.pop()
del list2[0]

# loop
list3 = ['a', 'b', 'c']
new_list = [x for x in list3 if 'a' in x]

new_list_1 = [x for x in range(10) if x < 5]
print(new_list_1)

# copy
copy_list = list3.copy()
print(copy_list)


# join
list4 = [1, 2]
list5 = ['a', 'b']
for x in list5:
    list4.append(x)

# list4.extend(list5)
