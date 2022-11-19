string = list(input())

stack = []

while string:
    stack.append(string.pop())
print(''.join(stack))