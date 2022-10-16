number = int(input())
points = 0
if number <= 100:
    points = 5
elif 100 <= number <= 1000:
    points = number * 0.2
elif number > 1000:
    points = number * 0.10
if number % 2 == 0:
    points = points + 1
elif number % 10 == 5:
    points = points + 2
print(points)
print(number + points)