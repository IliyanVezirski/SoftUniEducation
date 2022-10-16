factor = int(input())
count = int(input())
numbers = []
number = 0
for i in range(count):
    number += factor
    numbers.append(number)

print(numbers)