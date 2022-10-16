first_couple = int(input())
second_couple = int(input())
end_first_couple = int(input())
end_second_couple = int(input())
is_prime_first = True
is_prime_second = True
for first in range(first_couple,first_couple + end_first_couple + 1):
    for prime in range(2, first):
        if first % prime == 0:
            is_prime_first = False
            break
    if is_prime_first:
        for second in range(second_couple, second_couple + end_second_couple + 1):
            for prime in range(2, second):
                if second % prime == 0:
                    is_prime_second = False
                    break
            if is_prime_second:
                print(f'{first}{second}')
            is_prime_second = True
    is_prime_first = True