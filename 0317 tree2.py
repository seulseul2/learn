def heapIn(value):
    global last
    # 먼저, 삽입할 마지막 인덱스를 구한 뒤, 값을 삽입한다.
    last += 1
    TREE[last] = value
    # 자식 노드 => last(마지막꺼니까) / 부모 노드 => c//2(이진 트리니까)
    c = last
    p = c//2
    while p>=1 and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        # 포지션 재설정. 다시 자식(원래부모) 부모(새로운부모 = 원래부모//2)
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

TREE = [0] * 7
lst = [4, 15, 20, 11, 19, 23]
# 마지막 위치를 표시할 변수
last = 0
for value in lst:
    heapIn(value)
    print(TREE)