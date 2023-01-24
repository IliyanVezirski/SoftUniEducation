def recursive_power(number: int, power: int):
    if power == 0:
        return 1
    return recursive_power(number, power - 1) * number

