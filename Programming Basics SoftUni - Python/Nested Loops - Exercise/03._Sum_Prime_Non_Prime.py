number = input()
prime_sum = 0
none_prime_sum = 0
while number != 'stop':
    number_int = int(number)
    is_prime = True
    if number_int < 0:
        print(f'Number is negative.')
        number = input()
        continue
    elif number_int > 3:
        for prime in range(2, number_int):
            if number_int % prime == 0:
                is_prime = False
                break
    if is_prime or (0 <= number_int <= 3):
        prime_sum += number_int
    else:
        none_prime_sum += number_int
    number = input()
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {none_prime_sum}')


