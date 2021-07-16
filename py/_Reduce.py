
#
import functools

letters = ["H", "E", "L", "L", "O"]
numbers = [1, 2, 3]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)
