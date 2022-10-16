number = input()
number_list = number.split()
numbers =[]
for i in number_list:
    i = int(i)
    i *= - 1
    numbers.append(i)
print(numbers)
