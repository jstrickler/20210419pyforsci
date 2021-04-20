# from pkg.pkg import module
# find john/misc/johnlib.py using sys.path
from john.misc import johnlib
import john
import sys

john.spam()
print(john.ANIMAL)
johnlib.spam()
johnlib.toast()

# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders under sys.prefix

for path in sys.path:
    print(path)
