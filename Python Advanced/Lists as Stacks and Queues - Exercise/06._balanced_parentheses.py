balanced = True
parentheses = input()
stack = []
for el in parentheses:
    if el == "[" or el == "(" or el == "{":
        stack.append(el)
    elif el == "]" or el == ")" or el == ")":
        if stack:
            el_to_check = stack.pop()
            if (el_to_check == "[" and el == "]") or (el_to_check == "(" and el == ")") or (
                    el_to_check == "{" and el == "}"):
                continue
            else:
                balanced = False
        else:
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")
