numbers = tuple(map(float, input().split()))

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
for number in unique:
    number_count = numbers.count(number)
    print(f"{number} - {number_count} times")