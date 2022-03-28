def selMin(preV):
    minV = 1000000000
    for y in range(5):
        for x in range(5):
            if minV > arr[y][x] and arr[y][x] > preV:
                minV = arr[y][x]
    return minV

arr = [[9, 28, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

dst = [[0] * 5 for _ in range(5)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0 # 방향 우측에서 시작
x = y = 0
