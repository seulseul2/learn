import sys
sys.stdin = open('input (9).txt')

def Ssum(n):
    if type(tree[n]) == list:
        Ssum(tree[n][1])
        Ssum(tree[n][2])
        if tree[n][0] == '+':
            tree[n] = tree[tree[n][1]] + tree[tree[n][2]]
        elif tree[n][0] == '-':
            tree[n] = tree[tree[n][1]] - tree[tree[n][2]]
        elif tree[n][0] == '*':
            tree[n] = tree[tree[n][1]] * tree[tree[n][2]]
        elif tree[n][0] == '/':
            tree[n] = tree[tree[n][1]] / tree[tree[n][2]]
        
for TC in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(1001)]
    for i in range(N):
        x = list(input().split())
        if len(x) == 2:
            tree[int(x[0])] = int(x[1])
        elif len(x) == 4:
            tree[int(x[0])].append(x[1])
            tree[int(x[0])].append(int(x[2]))
            tree[int(x[0])].append(int(x[3]))
    Ssum(1)
    print('#{} {}' .format(TC, int(tree[1])))