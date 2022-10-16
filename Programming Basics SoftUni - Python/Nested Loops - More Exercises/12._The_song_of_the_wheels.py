control_number = int(input())
counter= 0
is_found = False
password = ''
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                if first < second and third > fourth and ((first * second) + (third * fourth) == control_number):
                    print(f'{first}{second}{third}{fourth}', end= " ")
                    counter += 1
                    if counter == 4:
                        password = str(first)+ str(second) + str(third) + str(fourth)
                        is_found = True
if is_found:
    print()
    print(f'Password: {password}')
else:
    print()
    print(f'No!')