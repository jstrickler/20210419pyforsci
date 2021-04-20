d1 = dict()  # empty dict
states = {'NC': 'Raleigh', 'IL': 'Springfield', 'CA': 'Sacramento'}
d3 = {}

print("states: {}\n".format(states))

states['NY'] = 'Albany'
states['BC'] = 'Victoria'
print("states: {}\n".format(states))

states['NY'] = 'Buffalo'
print("states: {}\n".format(states))

print(states['CA'])

print(states.get('OR'))
print(states.get('IL'))
print(states.get('MO', 'NOT FOUND'))
print(states.get('TX', 22))

print(states.setdefault('ME', 'Augusta'))
print(states.setdefault('NC', 'Durham'))
print()

print("states: {}\n".format(states))

print(len(states))

del states['BC']

print("states: {}\n".format(states))

for k in 'NC', 'TX', 'MT', 'CA', 'ME', 'MS':
    print(k, k in states)
print()

for state, capital in states.items():
    print(state, capital)
print()

print(states.items())

print(states.keys())
print(states.values())
print()

for item in states:
    print(item)
print()

a = {'a': 5, 'b': 10, 'c': 15}
b = [('a', 5), ('b', 10), ('c', 15)]

for letter, number in a.items():
    print(letter, number)
print()

for letter, number in b:
    print(letter, number)
print()









