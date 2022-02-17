def BruteForce(p, t):
    i = 0 # t의 검색 인덱스
    j = 0 # p의 검색 인덱스
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1

T = int(input())
for i in range(T):
    p = input()
    t = input()
    print(BruteForce(p, t))