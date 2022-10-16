number = input().split(", ")
palindrome = False
def even_number(numbers):
    half_of_number = len(i) // 2
    left_half = i[half_of_number::-1]
    right_half = i[half_of_number:]
    if left_half == right_half:
        palindrome = True
    else:
        palindrome = False
    print(palindrome)

def odd_number(numbers):
    half_of_number = len(i) // 2
    left_half = i[half_of_number-1::-1]
    right_half = i[half_of_number:]
    if left_half == right_half:
        palindrome = True
    else:
        palindrome = False
    print(palindrome)

for i in number:
    if len(i) % 2 == 0:
        odd_number(i)
    else:
        even_number(i)
