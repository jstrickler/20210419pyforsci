
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f1 = [f.upper() for f in fruits]  # implied append() of f.upper()
print("f1: {}\n".format(f1))

#  [EXPR for VAR in ITERABLE]
#  [EXPR for VAR in ITERABLE if CONDITION]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

f3 = [f for f in fruits if f.startswith('p') if len(f) > 5]
print("f3: {}\n".format(f3))

f3 = [f.upper()[:4] for f in fruits if f.startswith('p') if len(f) > 5]
print("f3: {}\n".format(f3))

#      (expr  for var in iterable if condition)
fgen = (f.upper() for f in fruits)
print(fgen)
for fruit in fgen:
    print(fruit)
print()








