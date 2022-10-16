int_passowrd = str(input())
int_passowrd = str.lower(int_passowrd)
passowrd = str.lower("s3cr3t!P@ssw0rd")
if int_passowrd == passowrd:
    print('Welcome')
else:
    print('Wrong password!')