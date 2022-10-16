number = int(input())
pure = True
for i in range(number):
    string = input()
    for j in range(0, len(string)):
        letter = string[j]
        if letter == ',' or letter == '.' or letter == '_':
            pure = False
    if pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
    pure = True