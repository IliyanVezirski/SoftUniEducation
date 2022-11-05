import re
text = input()
email = r"((?<=\s)([a-z0-9])([a-z0-9\._-])+@([a-z])+?[.-][a-z.]+\b)"

email_to_print = re.findall(email, text)

for el in range(len(email_to_print)):
    print(f"{email_to_print[el][0]}")