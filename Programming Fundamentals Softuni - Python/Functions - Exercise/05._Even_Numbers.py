def even_numbers(number: list):
    evens = [n for n in number if n % 2 == 0]
    return evens


numbers = input()
numbers = numbers.split(" ")
numbers_int = [int(n) for n in numbers]
print(even_numbers(numbers_int))
