budget = int(input())
purchase = input()
lenght = len(purchase)
price = 0
count_ticket = 0
count_other = 0
total_price = 0
while purchase != "End":
    lenght = len(purchase)
    diff = budget - total_price
    if lenght > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        total_price += price
        if diff >= price:
            count_ticket += 1
    else:
        price = ord(purchase[0])
        total_price +=price
        if diff >= price:
            count_other += 1
    if total_price > budget:
        break
    purchase = input()

print(count_ticket)
print(count_other)