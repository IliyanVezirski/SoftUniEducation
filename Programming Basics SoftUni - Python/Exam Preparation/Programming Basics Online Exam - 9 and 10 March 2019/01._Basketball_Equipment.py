price = int(input())
price_for_socks = price * 0.60
price_for_outfit = price_for_socks * 0.80
basketball_balls = price_for_outfit / 4
basketball_accessories = basketball_balls / 5
total = price + price_for_socks + price_for_outfit + basketball_balls + basketball_accessories
print(f'{total:.2f}')