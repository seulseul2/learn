def insert(value):
    p = 1
    while TREE[p]:
        if TREE[p] < value:
            p = p*2+1
        else:
            p = p*2
    TREE[p] = value

# 찾았으면 1을 return하고 못찾으면 0을 return
def find(key):
    p = 1
    while TREE[p]:
        if TREE[p] == key:
            return 1
        elif TREE[p] < key:
            p = p*2+1
        else:
            p = p*2
    return 0

def del(value):
    # 1. value의 위치를 찾아서
    # 2. 자식노드를 확인한다.
    # 3. 자식 노드가 없으면 TREE[pos] = 0
    # 4. 자식 노드가 한 개 있는 경우 -> 한칸 올려주면 됨. 근데 이게 말로는 쉽지만 구현은 상당히 번거롭다.
    # 5. 자식 노드가 두 개 있는 경우 -> 2가지 경우 가능. 9 - 3 - 6(오른쪽) or 9 - 6 - 3(왼쪽)

lst = [3, 5, 7, 4, 2, 6]
TREE = [0]*100
for value in lst:
    insert(value)
    print(TREE)