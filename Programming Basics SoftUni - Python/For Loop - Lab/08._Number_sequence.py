numbers = int(input())
max_number = -9999999999999999
min_number = 99999999999999999
for i in range(1, numbers + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    if min_number > number:
        min_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')