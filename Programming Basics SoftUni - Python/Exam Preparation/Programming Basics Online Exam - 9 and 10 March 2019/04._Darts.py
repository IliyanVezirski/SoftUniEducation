player_name = input()
total_points = 0
is_winner = False
successful_counter = 0
unsuccessful_counter = 0
difference = 301
while True:
    field = input()
    if field == 'Retire':
        break
    points = int(input())
    if field == 'Single':
        points = points
    elif field == 'Double':
        points *= 2
    elif field == 'Triple':
        points *= 3
    if points <= difference:
        successful_counter += 1
    else:
        unsuccessful_counter += 1
        continue
    difference = difference - points
    if difference == 0:
        is_winner = True
        break
if is_winner:
    print(f'{player_name} won the leg with {successful_counter} shots.')
else:
    print(f'{player_name} retired after {unsuccessful_counter} unsuccessful shots.')