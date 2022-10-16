money_needed = int(input())
sum_transactions = 0
counter = 0
cash_transaction = 0
terminal_transaction = 0
sum_cash_transaction = 0
sum_terminal_transaction = 0
transaction = ''
while sum_transactions < money_needed != 0:
    transaction = input()
    counter += 1
    if transaction == 'End':
        break
    else:
        transaction = int(transaction)
    if counter % 2 != 0:
        if transaction <= 100:
            cash_transaction += 1
            sum_transactions += transaction
            sum_cash_transaction += transaction
            print(f'Product sold!')
        else:
            print(f'Error in transaction!')
    else:
        if transaction >= 10:
            terminal_transaction += 1
            sum_transactions += transaction
            sum_terminal_transaction += transaction
            print(f'Product sold!')
        else:
            print(f'Error in transaction!')
if cash_transaction != 0:
    average_transaction_cash = sum_cash_transaction / cash_transaction
else:
    average_transaction_cash = 0
if terminal_transaction != 0:
    average_transaction_terminal = sum_terminal_transaction / terminal_transaction
else:
    average_transaction_terminal = 0
if transaction != 'End' and money_needed <= sum_transactions:
    print(f'Average CS: {average_transaction_cash:.2f}')
    print(f'Average CC: {average_transaction_terminal:.2f}')
else:
    print(f'Failed to collect required money for charity.')