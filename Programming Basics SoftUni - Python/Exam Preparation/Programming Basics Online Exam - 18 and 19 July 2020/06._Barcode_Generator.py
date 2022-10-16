number_one = input()
number_two = input()
second_range_1 = int(number_one[1])
second_range_2 = int(number_two[1])
third_range_1 = int(number_one[2])
third_range_2 = int(number_two[2])
fourth_range_1 = int(number_one[3])
fourth_range_2 = int(number_two[3])

for first in range(int(number_one[0]), int(number_two[0]) +1):
    if first % 2 == 1:
        for second in range(second_range_1, second_range_2+1):
            if second % 2 == 1:
                for third in range(third_range_1, third_range_2 +1):
                    if third % 2 == 1:
                        for fourth in range(fourth_range_1, fourth_range_2+1):
                            if fourth % 2 == 1:
                                print(f'{first}{second}{third}{fourth}', end=' ')