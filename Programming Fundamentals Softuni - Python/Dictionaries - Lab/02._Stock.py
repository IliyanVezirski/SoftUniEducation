elements = input().split()
elements_to_search = input().split()
element_dict = {}

for i in range(0,len(elements),2):
    key = elements[i]
    value = elements[i + 1]
    element_dict[key] = value
for n in elements_to_search:
    if n in element_dict:
        print(f"We have {element_dict[n]} of {n} left")
    else:
        print(f"Sorry, we don't have {n}")