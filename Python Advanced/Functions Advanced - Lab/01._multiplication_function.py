def multiply(*args):
    numbers = [int(i) for i in args]
    result = numbers[0]
    numbers.remove(result)
    for number in numbers:
        result *= number
    return result
