actor = "Chris Hemsworth"   # instance of the str class

print(type(actor), len(actor))

print(actor.upper())

a = actor.upper()
print(a)

print(actor.count('h'))
print(actor.count('swor'))
print(actor.lower().count('h'))

print(actor.find('Chris'))
print(actor.find('Liam'))
print(actor.swapcase())

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

print('worth' in actor)
print('hem' in actor)
print('hem' in actor.lower())

s1 = "      All my exes live in Texas      "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()

s2 = "xxxyyyxyxxyyAll my exes live in Texasyyyyyyyxxxxxxxx"
print("|" + s2.lstrip("xy") + "|")
print("|" + s2.rstrip("xy") + "|")
print("|" + s2.strip("xy") + "|")
print()











