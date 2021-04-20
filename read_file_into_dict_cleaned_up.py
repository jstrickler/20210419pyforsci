from pprint import pprint

# Huzzah! No mutable global data
FILE_PATH = 'DATA/knights.txt'

def main():
    kdata = read_data()
    pretty_print_knights(kdata)
    print_titles_and_names(kdata)
    print(get_value(kdata, 'Arthur', 1))


def read_data():
    knight_data = {}

    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')

            knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print_knights(data):
    # < 3.8
    pprint(data)
    # >=3.8
    # pprint(data, sort_dicts=False)
    print()

def print_titles_and_names(data):
    for name, fields in data.items():
        # name is key
        # data is value (i.e., tuple of 4 values)
        print(fields[0], name)
    print()

def get_value(data, knight, field):
    return data[knight][field]

if __name__ == '__main__':
    main()

