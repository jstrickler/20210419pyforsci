
f1 = ['eggs', 'bacon', 'waffles', 'pancakes',
      'scrapple', 'sausage']

f2 = ['bacon', 'waffles', 'toast', 'mushrooms', 'sausage',
      'bacon', 'toast', 'Danish', 'doughnuts']

set1 = set(f1)
set2 = set(f2)

print("set1:", set1)
print("set2:", set2)
print()

print("both:", set1 & set2) # intersection
print("just one:", set1 ^ set2)  # Xor
print("either:", set1 | set2) # union
print("just set1:", set1 - set2)
print("just set2:", set2 - set1)




