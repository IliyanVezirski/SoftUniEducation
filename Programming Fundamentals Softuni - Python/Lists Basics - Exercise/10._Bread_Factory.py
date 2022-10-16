initial_energy = 100
initial_coin = 100
events_in_list = input().split('|')
events = []
more_energy = 0
more_coin = 0
is_broken = False
energy_needed = 0
for i in events_in_list:
    events = i.split('-')
    if events[0] == 'rest':
        more_energy = events[1]
        more_energy = int(more_energy)
        if initial_energy + more_energy > 100:
            more_energy = 100 - initial_energy
            initial_energy = 100
        else:
            initial_energy += more_energy
        print(f"You gained {more_energy} energy.")
        print(f'Current energy: {initial_energy}.')
    elif events[0] == 'order':
        more_coin = events[1]
        more_coin = int(more_coin)
        if initial_energy - 30 >= 0:
            initial_coin += more_coin
            print(f'You earned {more_coin} coins.')
            initial_energy -= 30
        else:
            initial_energy += 50
            print(f'You had to rest!')
    else:
        more_coin = events[1]
        more_coin = int(more_coin)
        if more_coin <= initial_coin:
            initial_coin -= more_coin
            print(f'You bought {events[0]}.')
        else:
            is_broken = True
            print(f'Closed! Cannot afford {events[0]}.')
            break
if not is_broken:
    print(f'Day completed!')
    print(f"Coins: {initial_coin}")
    print(f"Energy: {initial_energy}")