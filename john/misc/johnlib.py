"""
John -- useful utilities to utilize for uncanny undeniable usefulness.

This contains some silly demo functions.
"""

COLORS = 'red', 'blue', 'purple', 'black', 'orange'

def main():
    """
    Program entry point.

    :return: None
    """
    spam()
    toast()
    for color in COLORS:
        print(color)
    print('-' * 60)


def spam():
    """
    Fatty meat stuff.

    :return: None
    """
    print("Hello from spam()")

def _ham():
    """
    Delicious pig leg (apologies to non-carnivores).

    :return: None
    """
    print("   and _ham()")

def toast():
    """
    Grilled bread which deserves butter and local honey.

    :return:  None
    """
    print("Hello from toast()")
    _ham()

if __name__ == '__main__':  # if I am not imported...
    main()
