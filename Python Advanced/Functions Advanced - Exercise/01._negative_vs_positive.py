def sum_negatives(numbers: list):
    sum_num = sum(i for i in numbers if i < 0)
    return sum_num


def sum_positive(numbers: list):
    sum_num = sum(i for i in numbers if i > 0)
    return sum_num


def print_numbers(number):
    negative_numbers = sum_negatives(number)
    positive_numbers = sum_positive(number)
    print(negative_numbers)
    print(positive_numbers)
    if abs(negative_numbers) < positive_numbers:
        print(f'The positives are stronger than the negatives')
    elif abs(negative_numbers) > positive_numbers:
        print(f'The negatives are stronger than the positives')


numbers = [int(i) for i in input().split()]
print_numbers(numbers)
