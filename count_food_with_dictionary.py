from pprint import pprint

food_counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        item = raw_line.rstrip()

        if item not in food_counts:
            food_counts[item] = 0

        food_counts[item] += 1
        # food_counts[item] = food_counts[item] + 1

pprint(food_counts)
