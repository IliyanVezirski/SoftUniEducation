numbers = input().split()
string = [n for n in input() if n]
number_to_remove = 0
message = []
for number in numbers:
    number_to_remove = 0
    for sum in number:
        sum = int(sum)
        number_to_remove += sum
    number_to_remove = number_to_remove % len(string)
    message.append(string[number_to_remove])
    string.pop(number_to_remove)


print(''.join(message))