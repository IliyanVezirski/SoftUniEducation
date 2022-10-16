def min_max_sum(numbers: str):
    sum_num = 0
    numbers_list = [int(n) for n in numbers.split(" ")]

    max_num = max(numbers_list)
    min_num = min(numbers_list)
    for n in numbers_list:
        sum_num += n
    final_min_max_sum = []
    final_min_max_sum.append(max_num)
    final_min_max_sum.append(min_num)
    final_min_max_sum.append(sum_num)
    return final_min_max_sum


number = input()

final_result = min_max_sum(number)

print(f'The minimum number is {final_result[1]}')
print(f"The maximum number is {final_result[0]}")
print(f"The sum number is: {final_result[2]}")