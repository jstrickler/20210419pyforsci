#!/usr/bin/env python
import numpy as np

a1 = np.arange(15)  # <1>
print("a1 shape", a1.shape)  # <2>
print()

print(a1)
print()

a1.shape = 3, 5  # <3>
print(a1)
print()

a1.shape = 5, 3  # <4>
print(a1)
print()

print(a1.flatten())  # <5>
print()

print(a1.transpose())  # <6>
print("------------------")

a2 = np.arange(40)  # <7>
a2.shape = 2, 5, 4  # <8>

print(a2)
print()

a2.shape = 2, 20
print("a2: {}\n".format(a2))
a2.shape = 4, 10
print("a2: {}\n".format(a2))
a2.shape = 2, 4, 5
print("a2: {}\n".format(a2))
a2.shape = 2, 2, 2, 5
print("a2: {}\n".format(a2))
