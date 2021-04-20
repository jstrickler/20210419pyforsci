from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')

        knight_data[name] = title, color, quest, comment

# < 3.8
pprint(knight_data)
# >=3.8
# pprint(knight_data, sort_dicts=False)
print()

for name, data in knight_data.items():
    # name is key
    # data is value (i.e., tuple of 4 values)
    print(data[0], name)
print()

print(knight_data['Robin'][1])

