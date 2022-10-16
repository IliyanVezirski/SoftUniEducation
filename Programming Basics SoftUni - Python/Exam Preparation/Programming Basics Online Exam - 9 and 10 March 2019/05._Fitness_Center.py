visitors_number = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
for visitors in range(visitors_number):
    activity = input()
    if activity == 'Back':
        back += 1
    elif activity == 'Chest':
        chest += 1
    elif activity == 'Legs':
        legs += 1
    elif activity == 'Abs':
        abs += 1
    elif activity == 'Protein shake':
        protein_shake += 1
    elif activity == 'Protein bar':
        protein_bar += 1
print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
percentage_people = ('%.2f' % ((back + chest + legs + abs) / visitors_number * 100))
percentage_drinks = ('%.2f'% ((protein_bar + protein_shake)/ visitors_number * 100))
print(f'{percentage_people}% - work out')
print(f'{percentage_drinks}% - protein')