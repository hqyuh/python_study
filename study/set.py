
this_set = {'a', 'b', 'c'}
print(len(this_set))


# add
# this_set.add('d')
# print(this_set)

this_set1 = {'d', 'e'}

# this_set.update(this_set1)


my_list = ['z', 'x']

this_set1.update(my_list)

print(this_set1)


# remove
this_set2 = {'x', 'y', 'z'}
this_set2.remove('x')
this_set2.discard('y')
print(this_set2)


# join
set1 = {'x'}
set2 = {1, 2}
set3 = set1.union(set2)
# set1.union(set2)
print(set3)


#
x = {'c', 'v', 'b'}
y = {'c', 'm'}


# trả về phần tử chung của 2 set
# x.intersection_update(y)
# z = x.intersection(y)

# trả về các phần tử không chung
x.symmetric_difference_update(y)
z = x.symmetric_difference(y)
print(x)






