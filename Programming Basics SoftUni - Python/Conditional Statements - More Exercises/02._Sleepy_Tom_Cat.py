holidays = int(input())
play_holidays = holidays * 127
play_working = (365 - holidays) * 63
minutes_per_year_for_play = play_working + play_holidays
left_minutes = abs(30000 - minutes_per_year_for_play)
left_minutes_hours = left_minutes // 60
left_minutes_minutes = left_minutes % 60
if minutes_per_year_for_play <= 30000:
    print('Tom sleeps well')
    print(f'{left_minutes_hours} hours and {left_minutes_minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{left_minutes_hours} hours and {left_minutes_minutes} minutes more for play')