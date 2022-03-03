N, M = map(int, input().split())
wood = list(map(int, input().split()))
start = min(wood)
end = max(wood)

while start <= end:
    middle = (start+end) // 2

    total = 0
    for x in wood:
        if x > middle:
            total += x - middle
    
    if total >= M:
        start = middle + 1
    else:
        end = middle - 1

print(middle)