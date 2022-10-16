import math

easter_bread = int(input())
max_flour = 0
max_sugar = 0
total_sugar_needed = 0
total_flour_needed = 0
for bread in range(easter_bread):
    sugar_needed = int(input())
    flour_needed = int(input())
    total_sugar_needed += sugar_needed
    total_flour_needed += flour_needed
    if sugar_needed > max_sugar:
        max_sugar = sugar_needed
    if flour_needed > max_flour:
        max_flour = flour_needed
sugar_packets_needed = math.ceil(total_sugar_needed / 950)
flour_packets_needed = math.ceil(total_flour_needed / 750)
print(f'Sugar: {sugar_packets_needed}')
print(f'Flour: {flour_packets_needed}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')