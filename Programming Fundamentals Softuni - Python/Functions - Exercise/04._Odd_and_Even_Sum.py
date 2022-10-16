def even_odd_sum(number):
    even_sum = 0
    odd_sum = 0
    number.split
    for i in number:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    numbers_for_return = []
    numbers_for_return.append(even_sum)
    numbers_for_return.append(odd_sum)
    return numbers_for_return

number = str(input())

numbers_for_print = even_odd_sum(number)


print(f'Odd sum = {numbers_for_print[1]}, Even sum = {numbers_for_print[0]}')