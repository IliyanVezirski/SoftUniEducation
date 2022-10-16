command = input()
coffee_needed = 0
total = 0
while command != "END":
    if command == command.upper():
        coffee_needed = 2
    else:
        coffee_needed = 1
    command = command.upper()
    if command == "CODING" or command == 'DOG' or command == "CAT" or command == "MOVIE":
        total += coffee_needed
    command = input()
if total > 5:
    print("You need extra sleep")
else:
    print(f'{total}')
