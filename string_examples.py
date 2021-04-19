s1 = "spam\n"
print(s1, type(s1), len(s1))

s2 = 'spam\n'
print(s2, type(s2), len(s2))

# good
print("Bob's my uncle")
print('Bob is my "uncle"')

# less good
print('Bob\'s my uncle')
print("Bob is my \"uncle\"")

s3 = """spam\n"""
s4 = '''spam\n'''

print('''Bob's my "uncle"''')

query = """
 select foo
 from bar
 where blah = 'bah'
"""

print(query)

s5 = r'spam\n'
print(s5)





