n = int(input())
for i in range(n):
    x = input()
    a = x.count('(')
    b = x.count(')')
    if a == b:
        if ')(' in x:
            
        print('YES')
    else:
        print('NO')