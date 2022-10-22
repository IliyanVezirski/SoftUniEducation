phone_book = {}

while True:
    numbers = input()
    if numbers.isdigit():
        numbers = int(numbers)
        break
    numbers = numbers.split('-')
    if numbers[0] not in phone_book:
        phone_book[numbers[0]] = numbers[1]


for i in range(numbers):
    name = input()
    if name not in phone_book.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phone_book[name]}")
