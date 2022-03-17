def heapIn(value):
    global last
    last += 1
    TREE[last] = value
    c = last
    p = c//2
    while p>=1 and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        # 포지션도 재설정 해줘야함
        c = p
        p = c//2

def heapPop():
    global last

    result = TREE[1]
    TREE[1], TREE[last] = TREE[last], TREE[1]
    TREE[last] = 0
    last -= 1

    p = 1
    # 자식노드 중 큰 값의 자식노드의 위치를 c에 넣어준다. 근데 조금 깔끔하게 쓰고 싶다면...? 
    c = p*2
    if c+1 <= last and TREE[c] < TREE[c+1]:
        c += 1
    
    while c<=last and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        p = c
        c = p*2
        if c+1 <= last and TREE[c] < TREE[c+1]:
            c += 1
        

    return result

TREE = [0] * 100
lst = [4, 15, 20, 11, 19, 23]
# 마지막 위치를 표시할 변수
last = 0
for value in lst:
    heapIn(value)
    print(TREE)