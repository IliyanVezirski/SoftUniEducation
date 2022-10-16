def rounding(nums):
    nums = str(nums)
    numbers = nums.split()
    numbers_int = []
    for i in numbers:
        i = float(i)
        i = round(i)
        numbers_int.append(i)
    print(numbers_int)


number = input()

rounding(number)