i = 0
while i < 3:
    print(i)
    i = i + 1
print()

while True:
    customer_name = input("Your name: ")
    if customer_name == 'q':
        break
    if customer_name == '':
        continue

    raw_num_tickets = input("Number of tickets: ")
    num_tickets = int(raw_num_tickets)
    print(f"{num_tickets} tickets reserved for {customer_name}")

