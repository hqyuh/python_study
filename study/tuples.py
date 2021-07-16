
my_tuples = ('a', 'b', 'c', 'd', 'e', 'f')

# print(len(my_tuples))

y = list(my_tuples)
y.append('g')
my_tuples = tuple(y)

print(my_tuples)

# remove
y.remove('a')
my_tuples = tuple(y)


#
# unpack
fruits = ('abc', 'def', 'rty', 'ghj')
(z, x, *c) = fruits

print(c)


# join
my_tuples1 = fruits * 2
print(my_tuples1)


my_tuples2 = (1, 2, 3, 1)
print(my_tuples2.count(1))


