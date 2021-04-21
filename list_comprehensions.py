
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

ff = [(f.upper(), len(f)) for f in fruits]
print("ff: {}\n".format(ff))

states = [('NC', 'Raleigh'), ('CA', 'Sacremento'), ('NY', 'Albany'),
          ('VA', 'Richmond')]

caps = [s[0] for s in states]
print("caps: {}\n".format(caps))

flat = [item for s in states for item in s]
print("flat: {}\n".format(flat))


