fruit = str(input())
set_size = str(input())
set_number = int(input())
Watermelon_small_price = 56 * 2
Mango_small_price = 36.66 * 2
Pineapple_small_price = 42.10 * 2
Raspberry_small_price = 20 * 2
Watermelon_big_price = 28.70 * 5
Mango_big_price = 19.60 * 5
Pineapple_big_price = 24.80 * 5
Raspberry_big_price = 15.20 * 5
if fruit == str('Watermelon') and set_size == str('small'):
    watermelon = float(Watermelon_small_price * set_number)
elif fruit == str('Mango') and set_size == str('small'):
    mango = float(Mango_small_price * set_number)
elif fruit == str('Pineapple') and set_size == str('small'):
    pineapple = float(Pineapple_small_price * set_number)
elif fruit == str('Raspberry') and set_size == str('small'):
    raspberry = float(Raspberry_small_price * set_number)
if fruit == str('Watermelon') and set_size == str('big'):
    watermelon = float(Watermelon_big_price * set_number)
elif fruit == str('Mango') and set_size == str('big'):
    mango = Mango_big_price * set_number
elif fruit == str('Pineapple') and set_size == str('big'):
    pineapple = Pineapple_big_price * set_number
elif fruit == str('Raspberry') and set == str('small'):
    raspberry = Raspberry_big_price * set_number
if fruit == str('Watermelon'):
    total_money = float(watermelon)
elif fruit == str('Mango'):
    total_money = float(mango)
elif fruit == str('Pineapple'):
    total_money = float(pineapple)
elif fruit == str('Raspberry'):
    total_money = float(raspberry)
if 400 <= total_money <= 1000:
    total_money = total_money * 0.85
elif total_money > 1000:
    total_money = total_money * 0.50
total_money_str = str('%.2f' % total_money)
print(f'{total_money_str} lv.')