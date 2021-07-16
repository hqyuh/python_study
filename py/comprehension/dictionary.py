# dictionary = {key: expression for (key, value) in iterable}


cities_in_F = {
    'New York': 32,
    'Boston': 75,
    'Los Angeles': 100
}
c = {key: (value + 2) for (key, value) in cities_in_F.items()}
print(c)

#
weather = {
    'New York': 'snowing',
    'Boston': 'sunny',
    'Los Angeles': 'sunny'
}

sunny_weather = {key: value for (key, value) in weather.items() if value == 'snowing'}
print(sunny_weather)

#
cities = {
    'New York': 32,
    'Boston': 75,
    'Los Angeles': 100
}

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(desc_cities)


#
def check_temp(value):
    if value >= 70:
        return "OK"


desc_cities1 = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities1)
