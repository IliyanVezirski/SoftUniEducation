rent = int(input())

figurine_price = rent * 0.70
catering_price = figurine_price * 0.85
sound_price = catering_price / 2

total_price = figurine_price + catering_price + sound_price + rent
print(f'{total_price:.2f}')