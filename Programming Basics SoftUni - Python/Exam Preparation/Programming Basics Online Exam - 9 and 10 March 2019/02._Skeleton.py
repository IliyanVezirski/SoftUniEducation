control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_for_100_m_length = int(input())
control_seconds = control_minutes * 60 + control_seconds
slower = length / 120 * 2.5
time_for_player = (length / 100 * seconds_for_100_m_length) - slower
diff = abs(time_for_player - control_seconds)
if time_for_player <= control_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_for_player:.3f}.')
else:
    print(f'No, Marin failed! He was {diff:.3f} second slower.')
