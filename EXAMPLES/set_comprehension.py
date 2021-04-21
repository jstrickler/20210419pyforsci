#!/usr/bin/env python
from collections import Counter
import re

with open("../DATA/alice.txt") as mary_in:
    s = {w.lower() for w in re.split(r'\W+', mary_in.read()) if w} #<1>
print(s)

alice_words = Counter(sorted(s))
print(alice_words)
