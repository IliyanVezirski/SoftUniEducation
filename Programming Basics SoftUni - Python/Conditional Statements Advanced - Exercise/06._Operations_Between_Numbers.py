n1 = int(input())
n2 = int(input())
operator = input()
sum = 0
eodd = ''
if operator == '+':
    sum = n1 + n2
elif operator == '-':
    sum = n1 - n2
elif operator == '*':
    sum = n1 * n2
if sum % 2 == 0:
   eodd = 'even'
else:
    eodd = 'odd'
if operator == '/':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        sum = n1 / n2
elif operator == '%':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        sum = n1 % n2
if operator == '+' or operator == '-' or operator == '*':
    print(f"{n1} {operator} {n2} = {sum} - {eodd}")
elif operator == '/' and n2 != 0:
    print(f"{n1} / {n2} ={('% .2f' % sum)}")
elif operator == '%' and n2 != 0:
    print(f"{n1} % {n2} = {sum}")