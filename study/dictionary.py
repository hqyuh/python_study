
this_dict = {
    'name': 'Mercedes CLG 300',
    'price': '5000'
}


# access
# x = this_dict['name']
x = this_dict.get('name')

# key
this_dict['brand'] = 'Mec'
print(this_dict.keys())

# change
# this_dict['price'] = '10000'
this_dict.update({'price': '20000'})
print(this_dict)

# remove
# this_dict.pop('price')
# this_dict.popitem()
del this_dict['price']
print(this_dict)

# loop



