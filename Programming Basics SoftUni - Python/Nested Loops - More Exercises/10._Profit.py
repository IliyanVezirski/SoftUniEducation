coins_1lv = int(input())
coins_2lv = int(input())
coins_5lv = int(input())
amount = int(input())
lv_1 = 0
lv_2 = 0
lv_5 = 0
for lv_1 in range(0, coins_1lv + 1):
    for lv_2 in range(0, coins_2lv + 1):
        for lv_5 in range(0, coins_5lv + 1):
            if lv_1 * 1 + lv_2 * 2 + lv_5 * 5 == amount:
                print(f'{lv_1} * 1 lv. + {lv_2} * 2 lv. + {lv_5} * 5 lv. = {amount} lv.')