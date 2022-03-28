import sys
input = sys.stdin.readline

n = int(input())
# 임시로 값을 받아줄 곳
tmp = [[] for _ in range(n+1)]
# 자식 노드부터 찾기 위한 리스트
level = [0 for _ in range(n+1)]
# servant lst
maxV = 0
servant_lst = [0 for _ in range(n+1)]

for i in range(n-1):
    p, c, value = map(int, input().split())
    level[p] += 1
    level[c] += 1
    tmp[c].append(p)
    tmp[c].append(value)

leaf = []
for j in range(len(level)):
    if level[j] == 1:
        leaf.append(j)

while 1:
    X = [[] for _ in range(n+1)]
    new_leaf = []
    for idx in leaf:
        X[tmp[idx][0]].append(tmp[idx][1])
        if tmp[idx][0] not in new_leaf:
            new_leaf.append(tmp[idx][0])
    cnt = 0
    for idx2 in range(len(X)):
        if len(X[idx2]) > 0:
                if sum(X[idx2]) > maxV:
                    maxV = sum(X[idx2])
                tmp[idx2][1] += max(X[idx2])
    leaf = new_leaf
    if not leaf:
        break
print(maxV)