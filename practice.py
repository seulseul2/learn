import sys

sys.stdin = open('input (2).txt')

for TC in range(1, 11):
    meaningless = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = arr[99].index(2)

    while y > 0:
        if x > 0 and arr[y][x-1] == 1:
            while x > 0 and arr[y][x-1] == 1: # 왼쪽으로 밀겠다 => 멈출때까지 조건문 걸어줘야함
                x -= 1
            else:
                y -= 1 # 여기서 -1 안해주면 다시 오른쪽으로 돌아감..

        elif x < 99 and arr[y][x+1] == 1:
            while x < 99 and arr[y][x+1] == 1:
                x += 1
            else:
                y -= 1
        else:
            y -= 1
    print('#{} {}' .format(TC, x))