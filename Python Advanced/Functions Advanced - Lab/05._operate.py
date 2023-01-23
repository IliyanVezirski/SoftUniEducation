def recursive_power(number: int, power: int):
    if power == 0:
        return number * number
    return recursive_power(number, power - 1)

print(recursive_power(2, 10))

print(2 ** 10)
