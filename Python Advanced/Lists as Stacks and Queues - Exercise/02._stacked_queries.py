stack = []
number = int(input())

for num in range(number):
    numbers = input()
    if numbers.startswith('1'):
        numbers = numbers.split()
        stack.append(int(numbers[1]))
    elif numbers.startswith('2'):
        if stack:
            stack.pop()
    elif numbers.startswith('3'):
        print(max(stack))
    elif numbers.startswith('4'):
        print(min(stack))
stack_to_print = []
while stack:
    stack_to_print.append(stack.pop())
print(*stack_to_print, sep=', ')