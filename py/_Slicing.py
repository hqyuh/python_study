name = "Bro Code"
# [start:end:step]

first_name = name[:3]         # [0:3]
last_name = name[4:]          # [4:end]
fun_name = name[::2]          # [0:end:2]
reversed_name = name[::-1]    # [0:end:-1]

print(reversed_name)

website1 = "http://github.com"
website2 = "http://google.com"

slice = slice(7, -4)

print(website2[slice])


name1 = "bro Code"

# if name1[0].islower():
#     name1 = name1.capitalize()
# print(name1)

first_name = name1[0:3].upper()
print(first_name)
