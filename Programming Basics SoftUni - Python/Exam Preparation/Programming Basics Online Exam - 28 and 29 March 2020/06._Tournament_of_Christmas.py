days = int(input())
total_win_count = 0
total_lose_count = 0
money_income = 0
win_day = 0
lose_day = 0
total_money = 0
for day in range(days):
    sport = input()
    win_count = 0
    lose_count = 0
    money_income = 0
    while sport != 'Finish':
        win_or_lose = input()
        if win_or_lose == 'Finish':
            break
        if win_or_lose == 'win':
            win_count += 1
            total_win_count += 1
            money_income += 20
        elif win_or_lose == 'lose':
            lose_count += 1
            total_lose_count += 1
    if win_count > lose_count:
        money_income *= 1.10
        total_money += money_income
        win_day += 1
    else:
        lose_day += 1
        total_money += money_income
if win_day > lose_day:
    total_money *= 1.20
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')