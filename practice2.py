def dfs(s):
    stack = [s]
    visited = [False] * 1001
    visited[s] = True
    cnt = 1
    while stack:
        start = stack.pop()
        for e in TREE[start]:
            if not visited[e]:
                stack.append(e)
                visited[e] = True
                cnt += 1
    return cnt

T = int(input())
for TC in range(1, T+1):
    E, N = map(int, input().split())
    TREE = [[] for _ in range(E+2)]
    T = list(map(int, input().split()))

    for i in range(0, len(T), 2):
        TREE[T[i]].append(T[i+1])
    print('#{} {}' .format(TC, dfs(N)))