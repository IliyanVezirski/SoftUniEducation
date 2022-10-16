n = int(input())
print('+ ' + ('- ' * (n-2)) + '+ ')
for i in range(1,n-1):
    print('| '+('- '*(n-2))+'| ')
print('+ ' + ('- ' * (n-2)) + '+ ')