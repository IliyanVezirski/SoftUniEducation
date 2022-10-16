n = int(input())
positive = []
negative = []
negative_sum =  0
positive_count = 0
for i in range(n):
    number = int(input())
    if number < 0:
        negative.append(number)
        negative_sum += number
    else:
        positive.append(number)
        positive_count += 1
print(f'{positive}')
print(f'{negative}')
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negative_sum}')
