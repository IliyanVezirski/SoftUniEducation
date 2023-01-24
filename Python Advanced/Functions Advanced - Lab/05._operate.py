def operate(operator, *args):
    if operator == '+':
        result = 0
        for i in args:
            result += i
        return result
    elif operator == "-":
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result
    elif operator == '*':
        result = 1
        for i in args:
            result *= i
        return result
    elif operator == '/':
        if args[0] == 0:
            result = args[1]
            for i in range(2, len(args)):
                result /= args[i]
            return result
        else:
            result = args[0]
            for i in range(1, len(args)):
                result /= args[i]
            return result

