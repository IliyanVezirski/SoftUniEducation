clients = int(input())
basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7
price = 0
purchase_counter = 0
total_purchases = 0
total_price_for_client = 0
total_price = 0
for client in range(clients):
    total_price_for_client = 0
    purchase_counter = 0
    while True:
        purchase = input()
        if purchase == 'Finish':
            break
        if purchase == 'basket':
            total_purchases += 1
            purchase_counter += 1
            price = basket_price
            total_price_for_client += price
        elif purchase == 'wreath':
            total_purchases += 1
            purchase_counter += 1
            price = wreath_price
            total_price_for_client += price
        elif purchase == 'chocolate bunny':
            total_purchases += 1
            purchase_counter += 1
            price = chocolate_bunny_price
            total_price_for_client += price
    if purchase_counter % 2 == 0:
        total_price_for_client *= 0.80
    total_price += total_price_for_client
    print(f'You purchased {purchase_counter} items for {total_price_for_client:.2f} leva.')
average = total_price / clients
print(f'Average bill per client is: {average:.2f} leva.')