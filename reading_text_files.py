file_path = "DATA/mary.txt"

file_obj = open(file_path, 'r')
print(file_obj)
file_obj.close()

# with EXPR:
# with EXPR as VAR:

with open(file_path) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n
        print(line)
# mary_in.close() is called automagically
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()  # read entire file to a str
    print("normal:")
    print(contents)
    print("raw:")
    print(repr(contents))
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    # all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/alice.txt') as alice_in:
    rabbit_count = 0
    for line_number, raw_line in enumerate(alice_in, 1):
        line = raw_line.rstrip()
        search_line = line.lower()
        if 'rabbit' in search_line:
            print(f"{line_number:4d}: {line}")
            rabbit_count += 1
print()
print(f"There were {rabbit_count} lines with 'rabbit'")
