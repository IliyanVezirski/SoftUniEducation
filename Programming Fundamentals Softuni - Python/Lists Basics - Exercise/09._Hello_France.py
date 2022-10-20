"""9.	* Hello, France
You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you
decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
You will receive a collection of items and a budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a specific price, which is given below:
Type	Maximum Price
Clothes	50.00
Shoes	35.00
Accessories	20.50
If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item,
 you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the
 budget after selling all the items is enough for buying the train ticket.
Input / Constraints
•	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the
range [0.00……1000.00]
•	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
Output
•	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
"{price1} {price2} {price3} … {priceN}"
•	Second, print the profit, formatted to the second decimal point in the following format:
"Profit: {profit}"
•	Finally:
o	If the budget is enough for buying the train ticket, print: "Hello, France!"
o	Otherwise, print: "Not enough money."
"""

items_to_sell = input().split('|')
budget = float(input())
cost_of_ticket = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.5
bought_items_price = []
for item_to_buy in items_to_sell:
    item_to_buy = item_to_buy.split('->')
    item = item_to_buy[0]
    price = float(item_to_buy[1])
    if budget < price:
        break
    if item == "Clothes":
        if price > clothes_max_price:
            continue
        else:
            bought_items_price.append(price)
            budget -= price
    elif item == "Shoes":
        if price > shoes_max_price:
            continue
        else:
            bought_items_price.append(price)
            budget -= price
    elif item == "Accessories":
        if price > accessories_max_price:
            continue
        else:
            bought_items_price.append(price)
            budget -= price

total_cost = sum(bought_items_price)
total = sum([i * 1.4 for i in bought_items_price])
profit = total - total_cost
total_money = total + budget
bought_items_price = [round(i*1.4,2) for i in bought_items_price]
print(* bought_items_price, sep=' ')
print(f"Profit: {profit:.2f}")
if budget + total >= cost_of_ticket:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")
