number = int(input())
print(' '* number + ' | ')
for i in range(1, number + 1):
    print(' '* (number - i)+ '*' * i + ' | ' + '*' * i + ' ' * (number - i))