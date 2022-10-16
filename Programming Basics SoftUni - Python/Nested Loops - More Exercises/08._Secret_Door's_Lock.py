first_number = int(input())
second_number = int(input())
third_number = int(input())
is_prime = False

for first in range(1, first_number + 1):
    for second in range(2, second_number + 1):
        is_prime = False
        for prime in range(2, second):
            if second % prime == 0:
                is_prime = True
            if second == 2:
                is_prime = False
            if is_prime:
                break
        if not is_prime:
            for third in range(1, third_number + 1):
                if first % 2 == 0 and third % 2 == 0:
                    print(f'{first} {second} {third}')