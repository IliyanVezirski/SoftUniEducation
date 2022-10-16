number = input()

numbers = number.split(" ")
numbers_int = [int(n) for n in numbers]
sorted_numbers = sorted(numbers_int)

print(sorted_numbers)