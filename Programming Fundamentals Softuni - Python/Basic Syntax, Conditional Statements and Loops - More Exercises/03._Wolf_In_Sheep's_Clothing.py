wolf_list = input()
wolf_list = list(wolf_list.split())
wolf_position = 0
sheep_position = 0
count = 0
for wolfs in reversed(wolf_list):
    count += 1
    if wolfs == 'wolf,' or wolfs == 'wolf':
        wolf_position = count
        sheep_position = wolf_position - 1
if wolf_position == 1:
    print(f'Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!')