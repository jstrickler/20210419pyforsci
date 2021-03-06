#!/usr/bin/env python
import json
from pprint import pprint

with open('../DATA/solar.json') as solar_in:  # <1>
    solar = json.load(solar_in)  # <2>

# json.loads(STRING)
# json.load(FILE_OBJECT)

# pprint(solar)

# print(solar['innerplanets'])  # <3>
# print('*' * 60)
# print(solar['innerplanets'][0]['name'])
# print('*' * 60)
for planet in solar['innerplanets'] + solar['outerplanets'] + solar['dwarfplanets']:
    print(planet['name'])

print("*" * 60)
for group in solar:
    if group.endswith('planets'):
        for planet in solar[group]:
            print(planet['name'])
            if planet['moons'] is not None:
                for moon in planet['moons']:
                    print(f"    {moon}")
