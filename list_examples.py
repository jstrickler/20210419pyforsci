list1 = list()  # empty list
list2 = ['a', 'b', 'c']
list3 = []

cities = ['Vancouver', 'Potomac', 'Ottawa']
print("cities: {}\n".format(cities))

cities.append('Durham')
cities.append('Schaumburg')
print("cities: {}\n".format(cities))

cities.insert(0, 'Columbia')
cities.insert(5, 'Chevy Chase')

print("cities: {}\n".format(cities))

more_cities = ['Raleigh', 'Albany', 'Toronto']
cities.extend(more_cities)
# not the same as:
# cities.append(more_cities)
print("cities: {}\n".format(cities))

del cities[0]
print("cities: {}\n".format(cities))

cities.remove('Durham')
print("cities: {}\n".format(cities))

city = cities.pop()
print("city: {}\n".format(city))
print("cities: {}\n".format(cities))

city = cities.pop(5)
print("city: {}\n".format(city))
print("cities: {}\n".format(cities))

print(cities[0], cities[-1])

print(cities[0:3])
print(cities[:3])

#  SEQ[START:STOP]   SEQ[START:STOP:STEP]

print(cities[2:5])
print(cities[3:])
print(cities[-3:])

c = "Chevy Chase"
print(c[:5])
print(c[6:])
print(c[2:4])
print(c[-4:])
print()

for city in cities:
    print(city)

# for VAR in ITERABLE:
#     # ???? VAR

for char in c:
    print(char.upper(), end=' ')
print('\n')

for char in c:
    print(char.upper(), end='*' if char != ' ' else ' ')
print('\n')

print(min(cities), max(cities))
print(sorted(cities))

print(len(cities))

r = reversed(cities)
for city in r:
    print(city)

r = reversed(cities)
print(r)
print(type(r))

list_a = ['A', 'B', 'C']
list_b = [10, 20, 30]
combo = zip(list_a, list_b)
print(combo)
for pair in combo:
    print(pair)

e = enumerate(cities)
print(e)
for i, city in e:  # [(0, X), (1, X), (2, X), ...]
    print(i, city)

# range(STOP) range(START, STOP), range(START, STOP, STEP)
r = range(10)
print(r)
for i in r:
    print(i)
print()




































