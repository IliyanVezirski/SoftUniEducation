numbers = [int(i) for i in input().split(", ")]
even_number = [n for n in range(len(numbers)) if numbers[n] % 2 == 0]
print(even_number)