import math
serial_name = input()
seasons_number = int(input())
episodes_number = int(input())
time_for_episode = float(input())
advertising = time_for_episode * 0.20
added_time = seasons_number * 10
total_time = (time_for_episode + advertising) * episodes_number * seasons_number + added_time
print(f'Total time needed to watch the {serial_name} series is {math.floor(total_time)} minutes.')