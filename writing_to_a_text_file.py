
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit + '\n')


with open('DATA/alice.txt') as alice_in:
    with open('ellie.txt', 'w') as ellie_out:
        for line in alice_in:
            new_line = line.replace("Alice", "Ellie")
            new_line = new_line.replace("ALICE", "ELLIE")
            ellie_out.write(new_line)

#   open(x, 'r')   read
#   open(x, 'w')   write
#   open(x, 'a')   append
#   open(x, 'x')   eXists ?? only open for writing if doesn't exist

#   open(x, 'rb')   read
#   open(x, 'wb')   write
#   open(x, 'ab')   append
#   open(x, 'xb')   eXists ?? only open for writing if doesn't
