import math

# business logic
def get_message():
    return "Hello, Python world"

m = get_message()

print(m)

# display logic  (AKA GUI or UX)
def show_message():
    msg = get_message()
    print(msg)

show_message()

def greet(whom):
    print("Hello,", whom)

greet("world")
greet("Mom!")
greet("sailor")

def area_circle(radius=1):
    return (radius ** 2) * math.pi

print(area_circle(5))
print(area_circle())
# print(area_circle(5, "wombat"))
print()

# cf. "python type hinting"
def triple(n: int) -> int:  # check with mypy
    return 3 * n

print(triple(5))
print(triple(math.pi))
print(triple('threat'))
print(triple(['moo']))

def doit(*files):
    print("doing it to:", files)


doit('wombat.txt')
doit('wombat.txt', 'woodchuck.txt', 'weasel.txt')
doit()

def locate(*, latitude=0, longitude=0):
    print(latitude, longitude)

locate(latitude=1.2, longitude=49)
locate(longitude=12, latitude=81.3)
locate()

def config(**kwargs):
    print("kwargs:", kwargs)

config(filename='wombats.txt', country="Bolivia",
       weapon="trebuchet")


def wacky(p1, p2, *p3, p4, p5, **p6):
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
print()

wacky(5, 10, 15, 20, 25, p4="wombat", color='green',
      food='pancakes', p5=30)












