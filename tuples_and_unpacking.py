person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

place = 'Durham', 'NC'

print(person[2], place[0])
print(person[:2])

def divmod(a, b):
    return a // b, a % b


x = divmod(37, 5)
print(x)
quotient, remainder = divmod(37, 5)
print(quotient, remainder)

states = [('NC', 'Raleigh'), ('CA', 'Sacremento'), ('NY', 'Albany'),
          ('VA', 'Richmond')]

print(states[0])
print(states[0][1])
print(states[0][1][3])

for state, capital in states:
    # state, capital = <next-element-of> states
    print(f"{capital} is the capital of {state}")
print()

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

# variable, ...                     = iterable
first_name, last_name, company, dob = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXt', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for _, last_name, *software, _ in people:
    print(last_name, software)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']

i, j, *k = values
print(i, j, k)

i, *j, k = values
print(i, j, k)

*i, j, k = values
print(i, j, k)

a = 1, 2, 3   # 3-tuple
b = 1, 2      # 2-tuple
c = 1,        # 1-tuple
d = ()        # 0-tuple

# {} (curly) braces
# [] (square) brackets
# () parentheses  (round brackets???)
# <> angle brackets










