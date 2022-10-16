budget = float(input())
season = input()
type_room = ''
room_cost = 0
location = ''
if budget <= 1000:
    type_room = 'Camp'
    if season == 'Summer':
        room_cost = budget * 0.65
        location = 'Alaska'
    else:
        room_cost = budget * 0.45
        location = 'Morocco'
elif 1000 < budget <= 3000:
    type_room = 'Hut'
    if season == 'Summer':
        room_cost = budget * 0.80
        location = 'Alaska'
    else:
        room_cost = budget * 0.60
        location = 'Morocco'
else:
    type_room = 'Hotel'
    if season == 'Summer':
        room_cost = budget * 0.90
        location = 'Alaska'
    else:
        room_cost = budget * 0.90
        location = 'Morocco'
print(f'{location} - {type_room} -{room_cost: .2f}')
