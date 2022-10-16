number_junior = int(input())
number_seniors = int(input())
trace_type = input()
tax_junior = 0
tax_seniors = 0
total_price = 0
if trace_type == 'trail':
    tax_seniors = number_seniors * 7
    tax_junior = number_junior * 5.50
elif trace_type == 'cross-country':
    tax_seniors = number_seniors * 9.50
    tax_junior = number_junior * 8
elif trace_type == 'downhill':
    tax_seniors = number_seniors * 13.75
    tax_junior = number_junior * 12.25
elif trace_type == 'road':
    tax_seniors = number_seniors * 21.50
    tax_junior = number_junior * 20
total_price = tax_seniors + tax_junior
if number_junior + number_seniors >= 50 and trace_type == 'cross-country':
    total_price *= 0.75
collected_money = ('%.2f' % (total_price * 0.95))
print(collected_money)