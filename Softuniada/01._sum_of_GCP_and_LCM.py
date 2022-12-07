number_1 = int(input())
number_2 = int(input())
biggest_number = max([number_1, number_2])
first_number_nod = []
second_number_nod = []

for number in range(1, number_1 + 1):
    if number_1 % number == 0:
        first_number_nod.append(number)
for number in range(1, number_2 + 1):
    if number_2 % number == 0:
        second_number_nod.append(number)
first_number_nod = sorted(first_number_nod, reverse=True)
second_number_nod = sorted(second_number_nod, reverse=True)
number_nod = 0
if first_number_nod >= second_number_nod:
    for number in first_number_nod:
        if number in second_number_nod:
            number_nod = number
            break
else:
    for number in second_number_nod:
        if number in first_number_nod:
            number_nod = number
            break
biggest_number = 0
number_to_check = max(number_1, number_2)
if number_to_check == number_1:
    number_to_add = number_1
else:
    number_to_add = number_2
number = 0
while True:
    if number_to_check % min(number_1, number_2) == 0 and number_to_check % max(number_1, number_2) == 0:
        number = number_to_check
        break
    number_to_check += number_to_add

print(number_nod + number)
