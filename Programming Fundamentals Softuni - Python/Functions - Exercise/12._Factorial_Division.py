number1 = int(input())
number2= int(input())
number1_factorial_numbers = []
number2_factorial_numbers = []
number1_factorial_sum = 1
number2_factorial_sum = 1
for i in range(number1, 0, -1):
    number1_factorial_numbers.append(i)

for n in range(number2, 0, -1):
    number2_factorial_numbers.append(n)

for j in number1_factorial_numbers:
    number1_factorial_sum *= j
for t in number2_factorial_numbers:
    number2_factorial_sum *= t

result = number1_factorial_sum / number2_factorial_sum
print(f'{result:.2f}')