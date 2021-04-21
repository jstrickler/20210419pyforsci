#!/usr/bin/env python
#!/Users/jstrick/opt/anaconda3/bin/python  note: can make your script fragile
import os
from pprint import pprint

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.lower(): len(a) for a in animals}  # <1>

print(d, '\n')

words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']

d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # <2>

for word, word_signature in d.items():
    print(word, word_signature)
print()

DIR = "../DATA"
file_info = {f: os.path.getsize(os.path.join(DIR, f)) for f in os.listdir(DIR)}
pprint(file_info)
