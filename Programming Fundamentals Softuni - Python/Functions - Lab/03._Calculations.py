operator = input()
num1 = int(input())
num2 = int(input())


def calculations(num1, num2, operator):
    result = 0
    if operator == "subtract":
        result = num1 - num2
    elif operator == 'divide':
        result = num1 // num2
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'multiply':
        result = num1 * num2
    return result


print(calculations(num1,num2,operator))