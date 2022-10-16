numbers = [int(i) for i in input().split(', ')]
number_max = max(numbers)
numbers_rows = 10
while numbers != []:
    numbers_rows_list = [i for i in numbers if i <= numbers_rows]
    index = 0
    print(f"Group of {numbers_rows}'s: {numbers_rows_list}")
    for i in numbers_rows_list:
        numbers.remove(i)
    numbers_rows += 10
