""""Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. Once you receive the type of customer you should print the receipt.
The taxes are 20% of each part's price you receive.
If the customer is special, he has a 10% discount on the total price with taxes.
If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.
If the total price is equal to zero, you should print "Invalid order!" on the console.
Input
•	You will receive numbers representing prices (without tax) until command "special" or "regular":
Output
•	The receipt should be in the following format:
"Congratulations you've just bought a new computer!
Price without taxes: {total price without taxes}$
Taxes: {total amount of taxes}$
-----------
Total price: {total price with taxes}$"
Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!
"""



parts_prices = input()

total = 0
while True:
    if parts_prices == 'special' or parts_prices == 'regular':
        break
    parts_prices = float(parts_prices)
    if parts_prices < 0 :
        print(f'Invalid price!')
        parts_prices = input()
        continue
    total += parts_prices
    parts_prices = input()

if total == 0:
    print(f'Invalid order!')
else:

    total_with_taxes = total * 1.2
    taxes = total * 0.2

    if parts_prices == 'special':
        total_with_taxes *= 0.90
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_with_taxes:.2f}$")

