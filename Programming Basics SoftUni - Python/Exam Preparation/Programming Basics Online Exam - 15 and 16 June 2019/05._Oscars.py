actor_name = input()
points_from_academy = float(input())
number_value = int(input())
total_points = points_from_academy
for value in range(number_value):
    name_value = input()
    points_from_value = float(input())
    points = (len(name_value) * points_from_value / 2)
    total_points += points
    if total_points >= 1250.5:
        break
    points = 0
diff = abs(total_points - 1250.5)
if total_points >= 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')