number = int(input())

number_divisors = []
number_divisors_sum = 0
for i in range(1,number):
    if number % i == 0:
        number_divisors.append(i)
for n in number_divisors:
    number_divisors_sum += n
if number_divisors_sum == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")