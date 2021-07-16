
usernames = ['Dude', 'Bro']
passwords = ('p@ssword', 'guest')

users = dict(zip(usernames, passwords))

for key, value in users.items():
    print(key + " : " + value)
