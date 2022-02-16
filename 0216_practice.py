t = 'This is a book~!'
p = 'is'

# patter이 text에 처음 나타난 위치를 return 합니다.
# pattern이 없으면 -1을 return
def Bru(pattern, text):
    N = len(text)
    M = len(pattern)
    i = j = 0

    while i<N and j<M:
        if text[i] != pattern[j]:
            i = i - j + 1
            #i = i + 1
            j = 0
        else:
            i += 1
            j += 1
    if j==M:
        return i-j
    else:
        return -1

print(Bru(p, t))