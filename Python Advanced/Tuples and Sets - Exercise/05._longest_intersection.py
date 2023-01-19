number_of_checks = int(input())
longest_intersection = []

for _ in range(number_of_checks):
    current_check = input().split('-')
    first_range = tuple(map(int, current_check[0].split(',')))
    second_range = tuple(map(int, current_check[1].split(',')))
    first_set = set(i for i in range(first_range[0], first_range[1] + 1))
    second_set = set(i for i in range(second_range[0], second_range[1] + 1))
    if len(first_set.intersection(second_set)) > len(longest_intersection):
        longest_intersection = list(first_set.intersection(second_set))
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
