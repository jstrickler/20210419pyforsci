from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Amelie")
d2 = CardDeck("Jordan")
try:
    d3 = CardDeck(3.14)
except TypeError as err:
    print(err)

print(d1)

print(d1.dealer_name)
print(d2.dealer_name)
# print(d3.dealer_name)

d1.dealer_name = 'Bob'
print(d1.dealer_name)

try:
    d2.dealer_name = None
except TypeError as err:
    print(err)
print()

d1.shuffle()
print(d1.cards)
for i in range(5):
    print(d1.draw())

print(d1.get_ranks())
print(CardDeck.get_ranks())

d1.bark()
CardDeck.bark()
print()

j1 = JokerDeck("Shamu")
j1.shuffle()
print(j1.dealer_name)
print(j1.cards)
print(j1.get_instructions())

print(JokerDeck.mro())

print(len(j1))
print(d1, j1)
