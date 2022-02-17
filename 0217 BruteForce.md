__BruteForce 함수 구현__

```python
def BruteForce(p, t):
    i = 0 # t의 검색 인덱스
    j = 0 # p의 검색 인덱스
    while i < len(t) and j < len(p): # j가 len(p)에 도착했다는 것은 탐색에 성공했다는 의미. 아닌데 i가 len(t)에 도착했다면 탐색 실패!
        if t[i] != p[j]:
            i = i-j # 처음에는 0-0, 1-1등 해서 0이지만, 그 다음부터는 1씩 2씩 차이가 나기 때문에 시작점을 다르게 설정할 수 있다.
            j = -1 # -1을 해주는 이유는 다시 +1을 해주면 0부터 시작하기 때문.
        i += 1
        j += 1
    if j == len(p):
        return i - len(p) # 찾은 지점에서 pattern 길이만큼 빼주면 시작점!
    else:
        return -1
```

--------------------

