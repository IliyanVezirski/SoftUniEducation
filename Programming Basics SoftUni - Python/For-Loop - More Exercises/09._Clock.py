hours = 0
minutes = 0


for hour in range(0, 24):
    hours = hour
    for minute in range(0, 60):
        minutes = minute
        for second in range(0, 60):
            seconds = second
            print(f'{hours} : {minutes} : {seconds}')