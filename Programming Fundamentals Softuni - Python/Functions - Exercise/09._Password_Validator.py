password = input()
password_len = False
password_alphanumeric = False
password_digits = False
counter = 0
if len(password) >= 6 and len(password) <= 10:
    password_len = True
if password.isalnum():
    password_alphanumeric = True
for i in password:
    if ord(i) >=48 and ord(i) <= 57:
        counter += 1
if counter >= 2:
    password_digits = True
if not password_len:
    print("Password must be between 6 and 10 characters")
if not password_alphanumeric:
    print("Password must consist only of letters and digits")
if not password_digits:
    print(f'Password must have at least 2 digits')

if password_digits == True and password_len == True and password_alphanumeric == True:
    print("Password is valid")