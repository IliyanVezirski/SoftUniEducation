number_of_elements = int(input())
elements = set()
for _ in range(number_of_elements):
    current_element = input().split()
    for element in current_element:
        elements.add(element)
print(*elements, sep='\n')
