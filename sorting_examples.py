fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

s = "WOMBAT"
print(str.lower(s), '\n')

f1 = sorted(fruits, key=str.lower)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)
print("f2: {}\n".format(f2))

def len_and_name(f):
    print(f"Item: {f:12s} Sort key: {len(f)}, {f.lower()}")
    return len(f), f.lower()

f3 = sorted(fruits, key=len_and_name)
print("f3: {}\n".format(f3))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    return p[3]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: p[3]):
    print(person)
print('-' * 60)

#  .....lambda param ...: return-value.......






