company_name = input()
tickets = int(input())
kid_tickets = int(input())
price_for_ticket = float(input())
expensese_for_service = float(input())
kid_tickets_price = price_for_ticket * 0.30 + expensese_for_service
tickets_price_with_service = price_for_ticket + expensese_for_service
total_tickets = tickets_price_with_service * tickets + kid_tickets * kid_tickets_price
total = total_tickets * 0.20
print(f'The profit of your agency from {company_name} tickets is {total:.2f} lv.')