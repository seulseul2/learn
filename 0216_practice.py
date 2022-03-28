import sys
input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

lst = []
for i in range(104):
    if isPrime(i):
        lst.append(i)
print(lst)

# x = int(input())
# for j in range(len(lst)-1):
#     if lst[j]*lst[j+1] > x:
#         print(lst[j]*lst[j+1])
#         break