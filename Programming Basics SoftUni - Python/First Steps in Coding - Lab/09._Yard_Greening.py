square = float(input())
square_price = square * 7.61
with_discount = square_price * 0.82
discount_price = square_price - with_discount
print(f"The final price is: {with_discount} lv.")
print(discount_price)