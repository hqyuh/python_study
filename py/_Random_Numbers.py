import random

x = random.randint(1, 6)
y = random.random()

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)

cards = [1, 2, 3, 4, 5, 'J', 'Q', 'K']
random.shuffle(cards)
print(cards)
