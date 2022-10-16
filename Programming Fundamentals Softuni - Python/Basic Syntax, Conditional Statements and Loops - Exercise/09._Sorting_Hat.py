name = input()
while True:
    if name == "Welcome!":
        print(f'Welcome to Hogwarts.')
        break
    if name == "Voldemort":
        print(f'You must not speak of that name!')
        break
    name_len = len(name)
    if name_len < 5:
        print(f'{name} goes to Gryffindor.')
    elif name_len == 5:
        print(f'{name} goes to Slytherin.')
    elif name_len == 6:
        print(f'{name} goes to Ravenclaw.')
    elif name_len > 6:
        print(f'{name} goes to Hufflepuff.')

    name = input()