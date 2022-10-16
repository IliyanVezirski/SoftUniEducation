record_in_seconds = float(input())
length = float(input())
time_for_one_met = float(input())
slower = length // 50 * 30
time = (time_for_one_met * length) + slower
diff = abs(time - record_in_seconds)
if time < record_in_seconds:
    print(f'Yes! The new record is {time:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')