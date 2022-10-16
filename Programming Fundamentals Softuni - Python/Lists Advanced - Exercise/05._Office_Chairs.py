rooms = int(input())
free_chairs = 0
free_space = True
for room in range(rooms):
    chairs_and_people = input().split()
    number_of_chairs = len(chairs_and_people[0])
    number_of_people = int(chairs_and_people[1])
    if number_of_people > number_of_chairs:
        print(f'{number_of_people - number_of_chairs} more chairs needed in room {room + 1}')
        free_space = False
    else:
        free_chairs += number_of_chairs - number_of_people
if free_space:
    print(f'Game On, {free_chairs} free chairs left')