def recursive_power(number: int, power: int):
    if power == 0:
        return 1
    return recursive_power(number, power - 1) * number

print(recursive_power(3, 10))

print(3 ** 10)
