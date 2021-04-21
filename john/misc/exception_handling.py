import logging

logging.basicConfig(filename="mylog.log")

file_name = 'devilslettuce.txt'

try:
    with open(file_name) as lettuce_in:
        pass
except FileNotFoundError as err:
    print(err)

items = ['cat', 'bird', 'dog', 'cow', 'moose']
try:
    print(items[99])
except IndexError as err:
    print(err)
print()

values = 5, 8, 0.0, "8.6", None, 14, 'abc', 2, 6

for v in values:
    try:
        num = float(v)
        result = 27 / num
    except (ValueError, ArithmeticError) as err:
        logging.exception("Uh-oh")
        print(err)
    except TypeError as err:
        print("TYPE!", err)
    else:
        print(result)
    finally:
        pass
        # disconnect, clean up data structure, etc

