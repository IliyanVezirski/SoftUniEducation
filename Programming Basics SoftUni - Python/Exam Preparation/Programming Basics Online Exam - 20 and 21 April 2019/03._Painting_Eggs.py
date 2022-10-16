size_eggs = input()
colour_eggs = input()
batch = int(input())
price = 0
if size_eggs == 'Large':
    if colour_eggs == 'Red':
        price = 16
    elif colour_eggs == 'Green':
        price = 12
    elif colour_eggs == 'Yellow':
        price = 9
elif size_eggs == 'Medium':
    if colour_eggs == 'Red':
        price = 13
    elif colour_eggs == 'Green':
        price = 9
    elif colour_eggs == 'Yellow':
        price = 7
elif size_eggs == 'Small':
    if colour_eggs == 'Red':
        price = 9
    elif colour_eggs == 'Green':
        price = 8
    elif colour_eggs == 'Yellow':
        price = 5
income = price * batch * 0.65
print(f'{income:.2f} leva.')