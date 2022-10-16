n = int(input())
number_lit = []
evevn_list = []
odd_list_list = []
negative_list = []
positive_list = []
for i in range(n):
    number = int(input())
    number_lit.append(number)

command = input()
if command == 'even':
    for j in number_lit:
        if j % 2 == 0:
            evevn_list.append(j)
    print(evevn_list)
elif command == 'odd':
    for j in number_lit:
        if j % 2 == 1:
            odd_list_list.append(j)
    print(odd_list_list)
elif command == 'negative':
    for j in number_lit:
        if j < 0:
            negative_list.append(j)
    print(negative_list)
elif command == 'positive':
    for j in number_lit:
        if j >= 0:
            positive_list.append(j)
    print(positive_list)
