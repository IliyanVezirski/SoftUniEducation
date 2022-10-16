import math
record = float(input())
metric = float(input())
time_in_second_metric = float(input())
slowly = (metric // 15) * 12.5
total_time = metric * time_in_second_metric + slowly
needed_time = abs(record - total_time)
remeining_time = abs(record - total_time)
if record > total_time:
    print(f"Yes, he succeeded! The new world record is{total_time: .2f} seconds.")
else:
    print(f"No, he failed! He was{needed_time: .2f} seconds slower.")