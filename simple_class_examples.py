
# instance = class(?args)
x = list()
y = list([1, 2, 3])
print(type(x), type(list))

#  self:Python::this:Java

class Dog:
    # class data goes here...
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof! woof!")
        self.breed = "English Shepherd"   # instance data

d1 = Dog("Nellie")
d2 = Dog("Andy")
d3 = Dog("Little Bear")

d1.bark()  # Dog.bark(d1)
d2.bark()  # Dog.bark(d2)
Dog.bark(d1) # don't do this....
print(d1.name)
print(d2.name)



