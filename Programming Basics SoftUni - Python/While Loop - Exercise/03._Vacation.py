budget = float(input())
money_on_hand = float(input())
spend_counter = 0
counter = 0
while spend_counter != 5:
    command = input()
    money = float(input())
    counter += 1
    if command == 'save':
        money_on_hand += money
        spend_counter = 0
    else:
        spend_counter += 1
        if money > money_on_hand:
            money_on_hand = 0
        else:
            money_on_hand -= money
    if spend_counter == 5:
        print(f"You can't save the money.")
        print(f'{counter}')
        break
    elif money_on_hand >= budget:
        print(f'You saved the money for {counter} days.')
        break
