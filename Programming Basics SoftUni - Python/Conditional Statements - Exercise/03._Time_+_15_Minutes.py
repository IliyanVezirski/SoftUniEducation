hour = int(input())
minutes = int(input())
minutes = minutes + 15
if minutes >= 60:
    minutes = minutes - 60
    hour = hour + 1
if hour >= 24:
    hour = hour - 24
if minutes < 10:
    print(f'{hour}:0{minutes}')
elif minutes >= 10:
    print(f'{hour}:{minutes}')