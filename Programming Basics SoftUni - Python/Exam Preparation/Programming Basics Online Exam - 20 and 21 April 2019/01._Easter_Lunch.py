easter_cake_count = int(input())
egg_loved = int(input())
cookie_kg = int(input())
total_price_easter_cake = easter_cake_count * 3.2
total_price_egg = egg_loved * 4.35
total_price_cookie = cookie_kg * 5.4
total_price_painting = (egg_loved * 12) * 0.15
total = total_price_easter_cake + total_price_egg + total_price_cookie + total_price_painting
print(f'{total:.2f}')