from collections import deque

sequence = input().split()
numbers_to_calculate = deque()

for number in sequence:
    result = 0
    if number.lstrip('-').isdigit():
        numbers_to_calculate.append(number)
    else:
        if number == '-':
            result = int(numbers_to_calculate.popleft())
            while numbers_to_calculate:
                result -= int(numbers_to_calculate.popleft())
            numbers_to_calculate.append(result)
        elif number == '*':
            result = int(numbers_to_calculate.popleft())
            while numbers_to_calculate:
                result *= int(numbers_to_calculate.popleft())
            numbers_to_calculate.append(result)
        elif number == '+':
            result = int(numbers_to_calculate.popleft())
            while numbers_to_calculate:
                result += int(numbers_to_calculate.popleft())
            numbers_to_calculate.append(result)
        elif number == '/':
            result = int(numbers_to_calculate.popleft())
            while numbers_to_calculate:
                result /= int(numbers_to_calculate.popleft())
            numbers_to_calculate.append(result)

print(int(result))